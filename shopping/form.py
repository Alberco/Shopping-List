from dataclasses import fields
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import User , DetailProduct
from django.contrib.auth.hashers import make_password

class LoginForm(forms.Form):
    user_email = forms.EmailField(max_length=254,label="Email ",required=True)
    user_password = forms.CharField(max_length=200,label="Password ",required=True,widget=forms.PasswordInput)
    
    user_email.widget.attrs.update({'class':
        'bg-white block mb-2 py-2 px-2 w-full mt-2 border-b-2  border-stone-800/50 outline-none focus:border-blue-800'})
    user_password.widget.attrs.update({'class':
        'bg-white block mb-2 py-2 px-2 w-full mt-2 border-b-2  border-stone-800/50 outline-none focus:border-blue-800'})
    
    
                        
class RegisterForm(ModelForm):
    user_password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput(
        attrs={
            'class' : 'bg-white block mb-2 py-2 px-2 w-full mt-2 border-b-2  border-stone-800/50 outline-none focus:border-blue-800',
            'placeholder' : 'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))
    
    class Meta:
        model = User
        fields = ('user_name','user_password','user_email')
        widgets = {
            'user_name':forms.TextInput(attrs={
                    'class':'bg-white block mb-2  px-2 w-full mt-2 border-b-2  border-stone-800/50 outline-none focus:border-blue-800',
                    'placeholder':'Ingrese Username',
                }
            ),
            'user_password':forms.PasswordInput(attrs={
                    'class':'bg-white block mb-2  px-2 w-full mt-2 border-b-2  border-stone-800/50 outline-none focus:border-blue-800',
                    'placeholder':'Ingrese Password',
                }
            ),
            'user_email':forms.EmailInput(attrs={
                    'class':'bg-white block mb-2  px-2 w-full mt-2 border-b-2  border-stone-800/50 outline-none focus:border-blue-800',
                    'placeholder':'Ingrese Email',
                }
            ),
        } 
        labels = {
            'user_name':('Username'),
            'user_password':('Password'),
            'user_email':('Email'),
        }
    
    def clean_user_password2(self):
        user_password = self.cleaned_data.get('user_password')                     
        user_password2 = self.cleaned_data.get('user_password2')
        if user_password != user_password2:
            raise forms.ValidationError("las contraseñas no son iguales")
        return user_password2
            

    def save(self,commit = True):
        instance = super(RegisterForm,self).save(commit=False)
        instance.user_password = make_password(self.cleaned_data.get('user_password'))
        if commit:
            instance.save()
        return instance
    
class NewListShoppingForm(forms.Form):
    shopping_description = forms.CharField(label="Description",max_length=200,required=True,widget=forms.Textarea(
        attrs={
            'class':'form-control',
        }
    ))

    
class NewProduct(forms.Form):
    detail_product_name = forms.CharField(label="Name Product",max_length=255,required=True,
    widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    detail_product_count = forms.CharField(label="Count Product",max_length=255,required=True,
    widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    detail_product_price = forms.FloatField(label="Count Product",required=True,
    widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'step': '0.01'
        }
    ))
    
    "timezone.now"