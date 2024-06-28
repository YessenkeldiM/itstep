from django.db import models

# Create your models here.

class User(models.Model):
    GENDER_TYPES = {
        'M': 'male',
        'F': 'female'
    }
    name = models.CharField(max_length=20, name='Name')
    surname = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_TYPES, max_length=20)
    adult = models.BooleanField()

# Есть модель предмет, у предмета есть тичер и есть ученики
# У учителя есть предметы
# у ученика предметы, у ученика есть группа и у группа есть классный руководитель, и 

