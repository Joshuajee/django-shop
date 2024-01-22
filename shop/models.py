from django.db import models
from django.utils.text import slugify

# Create your models here.
class Products (models .Model):
    name = models.CharField (max_length=50)
    description = models.TextField()
    slug = models.SlugField (db_index=True, blank=True, max_length = 250)
    product_img = models.FileField (upload_to ="product-img")
    price = models.FloatField()
    quantity = models. IntegerField()


    def save(self, *args, **kwargs) :
        slug = self.name
        self.slug = slugify(self.name+ "-"+ slug)
        return super().save(*args, **kwargs)