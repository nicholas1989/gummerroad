from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(blank=True, null=True, upload_to="product_covers/")
    slug = models.SlugField(null=True, blank=True)
    
    # content
    content_url = models.URLField(blank=True, null=True)
    content_file = models.FileField(blank=True, null=True)
    
    price = models.PositiveIntegerField(default=1) # cents
    
    def __str__(self):
        return self.name