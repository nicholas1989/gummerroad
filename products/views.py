from .models import Product
from django.views import generic

# Create your views here.
class ProductListView(generic.ListView):
    template_name = "discover.html"
    queryset = Product.objects.all()