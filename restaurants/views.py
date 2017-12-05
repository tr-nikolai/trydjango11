from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Restaurant
from .forms import RestaurantCreateModelForm


@login_required(login_url='/login/')
def restaurant_createview(request):
    template_name = 'restaurants/form.html'
    form = RestaurantCreateModelForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/rest/')
        else:
            return HttpResponseRedirect('/login/')
    context = {'form': form}
    return render(request, template_name, context)


def restaurant_listview(request):
    template_name = 'restaurants/rest_list.html'
    queryset = Restaurant.objects.all()
    context = {'restaurants': queryset}
    return render(request, template_name, context)


class RestauratListView(ListView):
    queryset = Restaurant.objects.all()

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Restaurant.objects.filter(
                Q(category__iexact=slug) |
                Q(category__iexact=slug)
            )
        else:
            queryset = Restaurant.objects.all()
        return queryset


class RestauratDetailView(DetailView):
    queryset = Restaurant.objects.all()

    # def get_object(self, *args, **kwargs):
    #     slug = self.kwargs.get('slug')
    #     obj = get_object_or_404(Restaurant, id=slug)
    #     return obj


class RestaurantCreateView(CreateView):
    form_class = RestaurantCreateModelForm
    template_name = 'restaurants/form.html'
    success_url = '/rest/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)