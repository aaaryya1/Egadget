# Generated by Django 4.2.3 on 2023-08-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('order placed', 'oderder placed'), ('shipped', 'shipped'), ('out for delivery', 'out for delivery'), ('Delivered', 'Delivered'), ('cancelled', 'cancelled')], default='Order placed', max_length=100),
        ),
    ]
