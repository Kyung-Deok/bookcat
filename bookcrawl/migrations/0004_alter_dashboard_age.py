# Generated by Django 4.0.5 on 2022-07-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcrawl', '0003_alter_dashboard_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='age',
            field=models.IntegerField(max_length=50),
        ),
    ]
