from django.db import models

# Create your models here.
class Book_data(models.Model):
    bookid = models.CharField(db_column='book_id', max_length=80)
    bookimgid = models.CharField(db_column='book_img_id', max_length=10)
    bookname = models.CharField(db_column='book_name', max_length=500)
    bookwritter = models.CharField(db_column='book_writter', max_length=50)
    bookmaker = models.CharField(db_column="book_maker", max_length=50)
    bookdate = models.DateField(db_column='book_date', auto_now=True)

    class Meta:
        db_table = 'bookbookdata'

class Dashboard(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    readingvolume = models.CharField(max_length=50)
    visit = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    cost = models.CharField(max_length=50, default=0)


    class Meta:
        db_table = 'board'