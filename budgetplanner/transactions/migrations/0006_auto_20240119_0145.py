# Generated by Django 3.2 on 2024-01-19 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_previous_migration_name'),
    ]

    operations = [
        migrations.RunSQL('ALTER TABLE transactions_monthlybudget ADD COLUMN new_column_name data_type;'),
    ]
