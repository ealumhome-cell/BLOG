from django.urls import path, include
from pages.views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home/", HomePageView.as_view(), name="homeTwo"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("posts", include('pages.urls'))
]



