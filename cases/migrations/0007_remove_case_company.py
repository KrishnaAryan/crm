# Generated by Django 3.1.7 on 2021-03-24 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0006_auto_20210323_1747"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="case",
            name="company",
        ),
    ]
