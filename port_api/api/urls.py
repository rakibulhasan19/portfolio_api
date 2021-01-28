
from django.urls import path
from .views import home_list_get

urlpatterns = [
    path('home/', home_list_get),
]
