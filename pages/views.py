from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView): #Class-based view
    #Object Oriented Porgramming - Inheritance
    template_name = "pages/home.html" #Link our view to the html

class AboutMePageView(TemplateView):
    template_name = "pages/about.html"