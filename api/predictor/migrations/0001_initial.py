# Generated by Django 3.2.9 on 2021-11-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='approvals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(max_length=50)),
                ('equipment_id', models.CharField(max_length=50)),
                ('completion_date', models.DateField()),
                ('action_recommendation_id', models.CharField(max_length=50)),
                ('action_recommendation_type', models.CharField(choices=[('art01', 'art01'), ('art02', 'art02'), ('art03', 'art03')], max_length=50)),
                ('action_recommendation_category', models.CharField(choices=[('arc01', 'arc01'), ('arc02', 'arc02'), ('arc03', 'arc03'), ('arc04', 'arc04'), ('arc05', 'arc05')], max_length=50)),
                ('equipment_area', models.CharField(max_length=50)),
                ('usage_type', models.CharField(choices=[('ut001', 'ut001'), ('ut002', 'ut002'), ('ut003', 'ut003'), ('ut004', 'ut004'), ('ut005', 'ut005'), ('ut006', 'ut006'), ('ut007', 'ut007'), ('ut008', 'ut008'), ('ut009', 'ut009'), ('ut010', 'ut010'), ('ut011', 'ut011'), ('ut012', 'ut012'), ('ut013', 'ut013')], max_length=50)),
            ],
        ),
    ]
