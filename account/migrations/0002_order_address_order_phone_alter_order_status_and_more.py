# Generated by Django 4.2.3 on 2023-08-09 06:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('oderder placed', 'oderder placed'), ('shipped', 'shipped'), ('out for delivery', 'out for delivery'), ('cancelled', 'cancelled')], default='Order placed', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'Product')},
        ),
    ]
