# Generated by Django 4.0.1 on 2022-08-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]