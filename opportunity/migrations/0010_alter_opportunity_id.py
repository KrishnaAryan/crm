# Generated by Django 3.2.11 on 2022-02-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0009_auto_20211006_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
