# Generated by Django 3.2.11 on 2022-02-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0019_auto_20211022_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
