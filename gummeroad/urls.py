from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
# from django.views.generic import TemplateView
from django.urls import path, include

from gum_road.views import Homepage, SignupView, verify_email
from gum_road.forms import EmailAuthenticationForm
from products.views import ProductListView, UserProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name="home_page")),
    path('', Homepage.as_view(), name='home_page'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('verify-email/<int:user_id>/',verify_email, name='verify_email'),
    path('login/', LoginView.as_view(authentication_form=EmailAuthenticationForm), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('discover/', ProductListView.as_view(), name="discover"),
    path('products/', UserProductListView.as_view(), name="user-products"),
    path('p/', include('products.urls', namespace='products')),
    path('gum_road/', include('gum_road.urls', namespace="gum_road")),
    # path('users/', include('users.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
