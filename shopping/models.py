from django.db import models
from django.contrib.auth.hashers import check_password
# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200,verbose_name="Username",unique=True)
    user_password = models.CharField(max_length=200,verbose_name="Password")
    user_email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.user_name
    
    def check_password_correction(self, attempted_password):
        return check_password(attempted_password,self.user_password)
    
    class Meta:
        db_table = "user"
    

class ListShopping(models.Model):
    shopping_description = models.CharField(max_length=200,verbose_name="Description Shopping")
    list_shopping_date = models.DateField(auto_now_add=True,verbose_name="Date Shopping")
    user_identificacion = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.shopping_description
    
    def newList(self,user):
        User.objects.create 
    
    class Meta:
        db_table = "list_shopping"
    
    
class DetailProduct(models.Model):
    detail_product_name = models.CharField(max_length=255,verbose_name="Product Name")
    detail_product_count = models.CharField(max_length=200,verbose_name="Count Product")
    detail_product_price = models.FloatField()
    lista_identificacion = models.ForeignKey(ListShopping,on_delete=models.CASCADE)

    def __str__(self):
        return self.detail_product_name

    class Meta:
        db_table = "detail_product"
    