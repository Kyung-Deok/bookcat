# Generated by Django 4.0.5 on 2022-07-04 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_books_book_data'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book_data',
            table='bookbookdata',
        ),
    ]
