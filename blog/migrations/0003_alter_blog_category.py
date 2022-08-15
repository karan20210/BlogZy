# Generated by Django 4.0.1 on 2022-08-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Sports', 'Sports'), ('Lifestyle', 'Lifestyle')], default='Technology', max_length=15),
        ),
    ]
