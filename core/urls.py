from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name ='index'),
    path('shop-grid.html', views.shop_grid, name='shop_grid'),
    path('shop-details.html', views.shop_details, name='shop_details'),
    path('shoping-cart.html', views.shoping_cart, name='shoping_cart'),
    path('contact.html', views.contact, name='contact'),
    path('checkout.html', views.checkout, name='checkout'),
    path('blog.html', views.blog, name='blog'),
    path('blog-details.html', views.blog_details, name='blog_details'),
]