# Generated by Django 2.2.7 on 2022-05-19 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0015_auto_20220519_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
