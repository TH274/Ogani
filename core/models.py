from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="cat", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class meta:
        verbose_name_plurel = "categories" 

    def category_image(self):
        return mark_safe('<img src="%s" width="50" hight="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

