from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=1000)
    category=models.CharField(max_length=100,default="")
    subcategory=models.CharField(max_length=100,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=3000)
    published_date=models.DateField()
    image=models.ImageField(blank=True, default="")

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    images=models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="shop/images")

    def __str__(self):
        return self.images.product_name

class ContactUs(models.Model):
    msg_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=100,default='')
    desc=models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.username

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    phone=models.CharField(max_length=13,default='')
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:7]+"..."