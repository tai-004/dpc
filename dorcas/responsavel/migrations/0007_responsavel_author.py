# Generated by Django 4.0.8 on 2023-02-24 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('responsavel', '0006_remove_responsavel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsavel',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
