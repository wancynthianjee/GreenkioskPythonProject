# Generated by Django 4.2.3 on 2023-07-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0002_product_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_ID', models.IntegerField()),
                ('list_of_items', models.IntegerField()),
                ('quantity_of_items', models.CharField(max_length=6)),
                ('products', models.ManyToManyField(to='inventory.product')),
            ],
        ),
    ]