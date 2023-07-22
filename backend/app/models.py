from django.db import models
from django.urls import reverse
from django.utils.text import slugify



class Product(models.Model):
    CATAGORY_CHOICES = (
        ('CR', 'Curd'),
        ('ML', 'Milk'),
        ('LS', 'Lassi'),
        ('MS', 'Milkshake'),
        ('PN', 'Paneer'),
        ('GH', 'Ghee'),
        ('CZ', 'Cheese'),
        ('IC', 'Ice-cream'),
    )

    title = models.CharField(verbose_name='Product title', max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    catagory = models.CharField(max_length=100, choices=CATAGORY_CHOICES)   
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_image = models.ImageField(upload_to='product')

    
    
    # def get_absolute_url(self):
    #     return reverse('app_name:url_name', kwargs={'slug': self.slug})
    #     # return '/postdetail/{self.slug}/


    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Products'


    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)


        # # convert image to desired size
        # img = Image.open(self.image.path)
        # if img.height > 300 or img.width > 300:
        #     converted_size = (300, 300)
        #     img.thumbnail(converted_size)
        #     img.save(self.image.path)

        super().save(*args, **kwargs)

    # Model string representation
    def __str__(self):
        return self.title