# Generated by Django 4.1.1 on 2022-09-18 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_blog',
            name='Blog_Image',
        ),
        migrations.RemoveField(
            model_name='user_registration',
            name='Image',
        ),
    ]
