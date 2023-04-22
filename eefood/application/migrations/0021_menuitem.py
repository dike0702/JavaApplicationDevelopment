# Generated by Django 3.2.9 on 2023-04-22 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0020_alter_favoriterestaurant_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='menu_images')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.restaurants')),
            ],
        ),
    ]