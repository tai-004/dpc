# Generated by Django 4.0.8 on 2023-02-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_profile_emailadm_alter_profile_funcaoadm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dtaDenascAdm',
            field=models.IntegerField(max_length=254, null=True),
        ),
    ]
