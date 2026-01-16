from django.urls import path
from django.views import HomePageView
from django.views import AboutMePageView

urlpatterns = [
    path("",HomePageView.as_view(), name="home"),
    path("home/"HomePageView.as_view(), name="homeTwo"),
    path("about/"AboutMePageView.as_view(), name="homeTwo"),
]



