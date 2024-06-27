from django.urls import path
from .views import Homepage

app_name = "gum_road"

urlpatterns = [
    path('', Homepage.as_view(), name='home_page'),
]
