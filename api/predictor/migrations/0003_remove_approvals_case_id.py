# Generated by Django 3.2.9 on 2021-11-20 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_approvals_equipment_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approvals',
            name='case_id',
        ),
    ]
