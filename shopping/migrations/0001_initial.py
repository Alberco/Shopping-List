# Generated by Django 4.0 on 2022-02-14 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, unique=True, verbose_name='Username')),
                ('user_password', models.CharField(max_length=200, verbose_name='Password')),
                ('user_email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='ListShopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopping_description', models.CharField(max_length=200, verbose_name='Description Shopping')),
                ('list_shopping_date', models.DateField(auto_now_add=True, verbose_name='Date Shopping')),
                ('user_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.user')),
            ],
            options={
                'db_table': 'list_shopping',
            },
        ),
        migrations.CreateModel(
            name='DetailProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_product_name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('detail_product_count', models.CharField(max_length=200, verbose_name='Count Product')),
                ('detail_product_price', models.FloatField()),
                ('lista_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.listshopping')),
            ],
            options={
                'db_table': 'detail_product',
            },
        ),
    ]
