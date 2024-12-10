from django.db import models
from email.policy import default
from unicodedata import decimal
from pyexpat import model
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User

STATUS_CHOICE = (
    ("process","Processing"),
    ("shipped","Shipped"),
    ("delivered","Delivered"),
)

STATUS = (
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("in_review","In Review"),
    ("published","Published"),
)

RATING = (
    (1,"Bad"),
    (2,"Pretty Bad"),
    (3,"Normal"),
    (4,"Good"),
    (5,"Very Good"),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="cat", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="Food")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class meta:
        verbose_name_plurel = "categories" 

    def category_image(self):
        return mark_safe('<img src="%s" width="50" hight="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    
class Tags():
    pass

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="Vend")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    description = models.TextField(null=True, blank=True, default="This is a vendor")

    address = models.CharField(max_length=100, default="123 Main Street")
    contact = models.CharField(max_length=100, default="+123 (456) 789")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")    
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class meta:
        verbose_name_plurel = "Vendors" 

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" hight="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="prd", alphabet="abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100, default="food")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    description = models.TextField(null=True, blank=True, default="This is a product")

    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="2.99")

    specification = models.DecimalField(null=True, blank=True)
    tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class meta:
        verbose_name_plurel = "Products" 

    def product_image(self):
        return mark_safe('<img src="%s" width="50" hight="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
 
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product.images", default="product.jpg")
    images = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plurel = "Products Images" 



class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

    class meta:
        verbose_name_plurel = "Cart Order" 
        
class CartOrderItems(models.Model):
    user = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")

    class meta:
        verbose_name_plurel = "Cart Order Items"

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" hight="50" />' % (self.image))


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plurel = "Product Review" 

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    

class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plurel = "Product Review" 

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating

