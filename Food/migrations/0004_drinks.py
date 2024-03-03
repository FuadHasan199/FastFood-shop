# Generated by Django 5.0.2 on 2024-03-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0003_burger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=4)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dImage', models.ImageField(upload_to='photos/drinkimage')),
            ],
        ),
    ]
