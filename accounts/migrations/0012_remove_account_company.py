# Generated by Django 3.1.7 on 2021-03-23 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_account_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="company",
        ),
    ]
