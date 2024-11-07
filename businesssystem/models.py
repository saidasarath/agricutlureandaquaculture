from django.db import models

# Create your models here.
class datetime1(models.Model):
    time12=models.TextField(max_length=225)
    class Meta:
        db_table="datetime1"
class contactus(models.Model):
    firstname=models.TextField(max_length=255)
    lastname=models.TextField(max_length=255)
    email=models.EmailField(primary_key=True)
    comment=models.TextField(max_length=255)
    class Meta:
        db_table="contactus"
class register(models.Model):
    username=models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    email = models.EmailField(primary_key=True)
    phonenumber=models.TextField(max_length=11)
    class Meta:
        db_table="register"
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)
    price = models.PositiveIntegerField(blank=False)
    image = models.FileField(blank=False,upload_to="productimages")

    def str(self):
        return self.name

    class Meta:
        db_table = "product_table"
