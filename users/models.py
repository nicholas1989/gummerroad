from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from products.models import Product
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    """Default user for gummeroad."""
    
    
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None # type: ignore
    last_name = None # type: ignore
    
    
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='group_user_set',  
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups'),
    )
    
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permission_set',  
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )
    
    
    
    def get_absolute_url(self):
        """Get url for user detail view.
        
        Returns:
            str: URL for user detail.
            
        """
        return reverse("users:detail", kwargs={"username": self.username})
    
 

class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="library")
    products = models.ManyToManyField(Product, blank=True)
    
    
    class Meta:
        verbose_name_plural = 'UserLibraries'
    
    def __str__(self):
        return self.user.email
       

