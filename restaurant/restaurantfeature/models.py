from django.db import models

# Create your models here.
class Category (models.Model):
    name=models.CharField( max_length=50)
    image=models.ImageField(upload_to='categoryimage/', default='default.jpg')
    
    def __str__(self):
        return self.name
    
    
    
class Product(models.Model):
    name=models.CharField( max_length=100)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE,default="1")
    price=models.DecimalField( max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='productimage/',  default='default.jpg')
    
    def __str__(self):
        return self.name
    
class Special(models.Model):
    name=models.CharField( max_length=100)
    description=models.CharField( max_length=150,  blank=True, null=True)
    price=models.DecimalField( max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='specialimage/',  default='default.jpg')
    
    def __str__(self):
        return self.name
    
    
class Testimonial(models.Model):
    name=models.CharField(max_length=150)
    description=models.CharField( max_length=300)
    image=models.ImageField(upload_to='testimonialimage/', default='default.jpg')
    
    def __str__(self):
        return self.name
    
    
class Chef(models.Model):
    name=models.CharField( max_length=150)
    profession=models.CharField(max_length=100)
    image=models.ImageField( upload_to='chefimage/',default='default.jpg')