
from django.urls import path
from .views import homeList,homeDetails,aboutList,aboutDetails

urlpatterns = [
    path('home/', homeList.as_view()),
    path('home/<int:id>/',homeDetails.as_view()),
    path('about/', aboutList.as_view()),
    path('about/<int:id>/',aboutDetails.as_view())
]
