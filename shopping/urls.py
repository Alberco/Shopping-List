from django.urls import path
from shopping.views import login , home , register ,list_shopping,logout,shopping,delete_product,update_product

urlpatterns = [
    path('product/',login ,name="login"),
    path('product/register',register,name="register"),
    path('product/home',home ,name="home"),
    path('product/home/list_shopping',list_shopping ,name="list_shopping"),
    path('product/logout',logout ,name="logout"),
    path('product/home/list_shopping/shopping/<int:id>',shopping ,name="shopping"),
    path('product/home/list_shopping/shopping/delete/<int:id>',delete_product ,name="delete_product"),
    path('product/home/list_shopping/shopping/update/<int:id>',update_product ,name="update_product"),
]
