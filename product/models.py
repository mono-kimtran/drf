from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})

    def get_products(self):
        return self.category_products.all()


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})

    def get_products(self):
        return self.brand_products.all()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='brand_products')
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, related_name='category_products', null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})
