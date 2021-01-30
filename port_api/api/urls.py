
from django.urls import path
from .views import homeList,homeDetails

urlpatterns = [
    path('home/', homeList.as_view()),
    path('home/<int:id>/',homeDetails.as_view())
]
