# Generated by Django 4.2.2 on 2023-07-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='signing_date',
            field=models.DateTimeField(blank=True),
        ),
    ]