# Generated by Django 3.1.6 on 2021-02-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=10),
        ),
    ]