from django.shortcuts import render
from django.views import View
from .models import Restaurant


def restaurant_listview(request):
    template_name = 'restaurants/rest_list.html'
    queryset = Restaurant.objects.all()
    context = {'restaurants': queryset}
    return render(request, template_name, context)
