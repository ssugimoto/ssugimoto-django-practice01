from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # ...
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # ...
    def __str__(self):
        return self.choice_text


class CompanyManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                select pc.name,count(*) from polls_company pc
                group by pc.name """)
            result_list = []
            for row in cursor.fetchall():
                p = self.model(name=row[0])
                p.num_responses = row[1]
                result_list.append(p)
            return result_list

    def allActive(self):
        """
            アクティブ状態を取得する
        :return: リスト
        """
        return self.filter(isactive=True)


class Company(models.Model):

    """
     参考サイト
     see https://python.keicode.com/django/model-data-access-basics.php

    """
    name = models.CharField(max_length=100)
    website = models.URLField(null=True)
    isactive = models.BooleanField(null=False,default=False)

    # objects = models.Manager() # Default manager
    objects = CompanyManager()

    def __str__(self):
        return self.name;


class Employee(models.Model):

    """

    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.lastname;


class Book(models.Model):
    # https://kurozumi.github.io/django-import-export/getting_started.html
    name = models.CharField('Book name', max_length=100)
    author_email = models.EmailField('Author email', max_length=75, blank=True)
    imported = models.BooleanField(default=False)
    published = models.DateField('Published', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __unicode__(self):
        return self.name

