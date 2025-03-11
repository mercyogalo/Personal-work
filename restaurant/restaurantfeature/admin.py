from django.contrib import admin
from . models import Category, Product, Special, Testimonial

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Special)
admin.site.register(Testimonial)