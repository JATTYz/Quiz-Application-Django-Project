# Generated by Django 2.2.7 on 2022-05-19 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0012_auto_20220519_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='score',
        ),
    ]