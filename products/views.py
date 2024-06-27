from typing import Any
from django.db.models.query import QuerySet
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.
class ProductListView(generic.ListView):
    template_name = "discover.html"
    queryset = Product.objects.all()
    
    
class ProductDetailView(generic.DetailView):
    template_name = "products/product.html"
    queryset = Product.objects.all()
    context_object_name = "product"
    
    
class UserProductListView(LoginRequiredMixin, generic.ListView):
    # shows the user's created products
    template_name = "products.html"
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)