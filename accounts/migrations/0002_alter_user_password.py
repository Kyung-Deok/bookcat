# Generated by Django 4.0.5 on 2022-07-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(db_column='password', max_length=600),
        ),
    ]
