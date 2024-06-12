from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
# from django.views.generic import TemplateView
from django.urls import path, include

from gum_road.views import home_page
from products.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name="home_page")),
    path('', home_page, name='home_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('discover/', ProductListView.as_view(), name="discover"),
    path('gum_road/', include('gum_road.urls', namespace="gum_road")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
