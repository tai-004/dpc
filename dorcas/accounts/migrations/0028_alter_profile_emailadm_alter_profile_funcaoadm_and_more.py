# Generated by Django 4.0.8 on 2023-02-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_profile_dtadefuncaoadm_profile_dtadenascadm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emailAdm',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='funcaoAdm',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
