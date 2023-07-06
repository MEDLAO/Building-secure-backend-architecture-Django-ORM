# Generated by Django 4.2.2 on 2023-07-02 09:54

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_employee', models.CharField(choices=[('Employee', 'Employee'), ('Manager', 'Manager')], max_length=8)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Management', 'Management'), ('Sales', 'Sales'), ('Support', 'Support')], max_length=10)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email_team', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True)),
            ],
        ),
    ]
