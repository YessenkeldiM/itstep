import datetime

from django.db import models
from django.utils import timezone
from django.db.models import F

class Measurements(models.TextChoices):
       FEET = 'FT'
       SANTIMETER = 'SM'
       MILLIMTER = 'MM'

class Measure(models.Model):
    measurement = models.CharField(choices=Measurements, max_length=50)

class Question(models.Model):
    QTYPE = {
        "O": "Open",
        "C": "Closed",
        "I": "Ilyas",
    }

    qtype = models.CharField(max_length=100, choices=QTYPE, help_text='ПАМАГИ!', verbose_name='Question name')
    question_text = models.CharField(max_length=200)
    comment = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateField('date published')

    class Meta:
        pass

    def __str__(self):
        # return self.question_text + '   ' +str(self.pub_date)
        return f'{self.question_text}   {str(self.pub_date)}'
    
    def was_published_recently(self):
        return self.pub_date > timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='choices_two')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
    class Meta:
        pass
    
    
class Person(models.Model):
    name = models.CharField(max_length=200)
