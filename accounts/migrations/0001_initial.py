# Generated by Django 4.0.5 on 2022-07-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='username', max_length=50)),
                ('password', models.CharField(db_column='password', max_length=50)),
                ('fullname', models.CharField(db_column='fullname', max_length=50)),
                ('useremail', models.CharField(blank=True, db_column='useremail', max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True, db_column='create_at')),
                ('update_at', models.DateTimeField(auto_now=True, db_column='update_at')),
            ],
            options={
                'db_table': 'serviceuser',
            },
        ),
    ]
