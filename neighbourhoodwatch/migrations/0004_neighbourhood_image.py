# Generated by Django 3.0.2 on 2020-02-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhoodwatch', '0003_neighbourhood_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pictures'),
        ),
    ]
