
from django.urls import path
from .views import home_list_get,home_details

urlpatterns = [
    path('home/', home_list_get),
    path('home/<int:pk>/',home_details)
]
