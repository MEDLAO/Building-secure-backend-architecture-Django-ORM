# Generated by Django 4.2.2 on 2023-07-15 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='sales_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_sales', to='staff.employee'),
        ),
        migrations.AddField(
            model_name='contract',
            name='support_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_support', to='staff.employee'),
        ),
    ]
