# Generated by Django 4.0.5 on 2022-07-06 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookcrawl', '0002_alter_dashboard_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dashboard',
            table='board',
        ),
    ]