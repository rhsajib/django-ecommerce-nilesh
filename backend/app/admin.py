from django.contrib import admin
from .models import Product

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):         
    list_display = ['id', 'title', 'catagory', 'discount_price', 'product_image']
    # list_display_links = ["title"]             
    # ordering = ['id']                          
    # search_fields = ['title', 'catagory']      
    # list_per_page = 10
