from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from .models import Restaurant
from .forms import RestaurantCreateForms, RestaurantCreateModelForm


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
