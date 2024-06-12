from django.urls import path
from .views import ProductListView

app_name = "products"

urlpatterns = [
    path('discover/',ProductListView.as_view() , name='discover'),
]