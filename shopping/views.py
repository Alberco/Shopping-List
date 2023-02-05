from django.shortcuts import redirect, render
from .models import User,ListShopping,DetailProduct
from .form import LoginForm ,RegisterForm ,NewListShoppingForm,NewProduct
from .tools.decoradores_perosonalizados import islogin_required

def login(request):
    if request.method == 'POST':
         form_login = LoginForm(request.POST)
         if form_login.is_valid():
            email = form_login.cleaned_data["user_email"] 
            password = form_login.cleaned_data["user_password"]
            verificar = User.objects.filter(user_email=email).first()
            if(verificar and verificar.check_password_correction(attempted_password=password)):
                request.session['username'] = email
                request.session['password'] = password
                return redirect(home)
    if request.session.get('username') != None and request.session.get('password') != None:
        return redirect('home')
    form_login=LoginForm()
    return render(request,'index.html',{'form_login':form_login})
            
def register(request):
    if request.method == 'POST':
        form_register = RegisterForm(request.POST)
        if form_register.is_valid():
            form_register.save()
            return redirect(login)
    form_register=RegisterForm()
    return render(request,'register.html',{'form_register':form_register})

@islogin_required
def home(request):
    return render(request,'home.html')

@islogin_required
def list_shopping(request):
    if request.method == 'POST':
        form_shopping = NewListShoppingForm(request.POST)
        if form_shopping.is_valid():
            description = form_shopping.cleaned_data["shopping_description"]
            user_data = request.session['username']
            query_user = User.objects.filter(user_email=user_data).first()
            list = ListShopping(shopping_description=description,user_identificacion=query_user)
            list.save()
            return redirect(list_shopping)
    query_list = ListShopping.objects.filter(user_identificacion__user_email=request.session['username'])
    form_shopping=NewListShoppingForm()
    content = {'query_list':query_list,
               'form_shopping':form_shopping}
    return render(request,'add_list.html',content)

@islogin_required
def shopping(request,id):
    if request.method == 'POST':
        form_product = NewProduct(request.POST)
        if form_product.is_valid():
            name = form_product.cleaned_data["detail_product_name"]
            count = form_product.cleaned_data["detail_product_count"]
            price = form_product.cleaned_data["detail_product_price"]
            query_shopping = ListShopping.objects.get(pk=id)
            product = DetailProduct(detail_product_name=name,detail_product_count=count,detail_product_price=price,lista_identificacion=query_shopping)
            product.save()
            return redirect(shopping,id)
    form_product = NewProduct()
    query_shopping = DetailProduct.objects.filter(lista_identificacion__id=id)
    content = {'query_shopping':query_shopping,
               'form_product':form_product}
    return render(request,'shopping.html',content)

@islogin_required
def delete_product(request,id):
    if request.method == 'GET':
        query_product = DetailProduct.objects.filter(id=id).first()
        query_product.delete()
    return redirect(list_shopping)

@islogin_required
def update_product(request,id):
    if request.method == 'POST':
        form_product = NewProduct(request.POST)
        if form_product.is_valid():
            name = form_product.cleaned_data["detail_product_name"]
            count = form_product.cleaned_data["detail_product_count"]
            price = form_product.cleaned_data["detail_product_price"]
            DetailProduct.objects.filter(id=id).update(detail_product_name=name,detail_product_count=count,detail_product_price=price)
        return redirect(list_shopping)
    form_product = NewProduct()
    product_list = DetailProduct.objects.get(pk=id)
    content = {'form_product':form_product,
                'product_list':product_list
    }
    return render(request,'update_product.html',content)
    
@islogin_required
def logout(request):
    del request.session["username"]
    del request.session["password"]
    return redirect(login)