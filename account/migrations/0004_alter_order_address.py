# Generated by Django 4.2.3 on 2023-08-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_cart_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
