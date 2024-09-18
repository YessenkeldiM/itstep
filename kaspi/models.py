from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.timezone import now
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# from django.contrib.postgres.fields import DateRangeField

from datetime import date

from .managers import *

# Create your models here.

class KaspiObject(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True, blank=True)
    create_date = models.DateField(default=now)
    # active_in = DateRangeField(verbose_name='Активно в промежутке', default=(now, '2024-12-12'))
    

    class Meta:
        abstract = True

class Good(KaspiObject):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.IntegerField()

    objects = models.Manager()
    custom_manager = CustomGoodManager()

    def __str__(self):
        return self.name


class Magazin(KaspiObject):
    address = models.CharField(max_length=256)
    goods = models.ManyToManyField(to=Good, through='MagazineGoods', through_fields=('magazine', 'good'))
    staff = models.ManyToManyField(to=User)

    # objects = models.Manager()
    # custom_manager = CustomMagazinManager()
    # custom_q_manager = CustomQueryset.as_manager()


    def __str__(self):
        return self.name
    
class SortedMagazin(Magazin):
    class Meta:
        proxy = True
        ordering = ['-create_date']


class MagazineGoods(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    magazine = models.ForeignKey(Magazin, on_delete=models.CASCADE)

    def __str__(self):
        return 'Magazine: ' + str(self.magazine) + ' ' + 'Good: ' + str(self.good)


class Review(models.Model):
    text = models.TextField(max_length=256)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')




def report_good_created(sender, **kwargs):
    print("Good is created!")

post_save.connect(report_good_created, sender=Good)

@receiver(post_delete, sender=Good)
def report_good_deleted(sender, **kwargs):
    print("Good is deleted!")


