# Generated by Django 4.2.2 on 2023-06-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_smartbase_admin', '0003_auto_20230402_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sbadminlistviewconfiguration',
            name='action',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sbadminlistviewconfiguration',
            name='modifier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
