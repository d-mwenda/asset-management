# Generated by Django 2.2 on 2019-09-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='components',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='assets',
            name='warranty_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
