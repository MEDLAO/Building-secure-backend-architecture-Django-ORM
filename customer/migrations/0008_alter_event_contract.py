# Generated by Django 4.2.2 on 2023-07-03 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_event_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='customer.contract', unique=True),
        ),
    ]