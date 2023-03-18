# Generated by Django 4.0.8 on 2023-02-21 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instituicao',
            name='user',
        ),
        migrations.AddField(
            model_name='instituicao',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]