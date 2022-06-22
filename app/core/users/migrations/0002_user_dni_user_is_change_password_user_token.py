# Generated by Django 4.0 on 2022-06-17 02:15

import core.users.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dni',
            field=models.CharField(default=1, max_length=13, unique=True, validators=[core.users.validators.vcedula], verbose_name='Cédula o RUC'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_change_password',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True),
        ),
    ]