# Generated by Django 4.2.3 on 2023-07-24 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(default='cart', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='product_image')),
                ('description', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('mobile phone', 'mobile phone'), ('earphone', 'earphone'), ('laptop', 'laptop'), ('tablet', 'tablet'), ('smart watch', 'smart watch'), ('BT speaker', 'BT speaker')], default='Mobile phone', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('oderder placed', 'oderder placed'), ('shipped', 'shipped'), ('out for delivery', 'out for delivery'), ('cancelled', 'cancelled')], max_length=100)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cartorders', to='account.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
