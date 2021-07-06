from django.db import models

# Create your models here.
class Categories(models.Model):
    description = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.description}"

class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="categoria")
    product_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.title}: {self.description} - ${self.price} - {self.category}"

class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True, related_name="productos_carrito")
    total = models.IntegerField()

    def __str__(self):
        return f"{self.products} - total: ${self.total}"
