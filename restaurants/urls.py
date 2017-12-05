from django.conf.urls import url
from .views import (restaurant_listview,
                    RestauratListView,
                    RestauratDetailView,
                    restaurant_createview,
                    RestaurantCreateView)

urlpatterns = [
    url(r'^$', RestauratListView.as_view()),
    # url(r'^(?P<slug>\w+)/$', RestauratListView.as_view()),
    url(r'^create/$',   restaurant_createview),
    # url(r'^create/$',   RestaurantCreateView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', RestauratDetailView.as_view()),
]
