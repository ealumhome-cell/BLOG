from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", HomePageView.as_view(), name="homeTwo"),
    path("about/", AboutPageView.as_view(), name="about")
]