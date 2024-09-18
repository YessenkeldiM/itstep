from django.db import models
from django.utils.timezone import now


class CustomQueryset(models.QuerySet):
    def filter_by_date(self):
        return self.filter(create_date__gte='2024-08-18')

class CustomGoodManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return CustomQueryset(self.model, using = self._db).filter_by_date()
    
# class CustomMagazinManager(models.Manager):
#     def get_queryset(self) -> models.QuerySet:
#         return CustomQueryset(self.model, using = self._db).filter_by_date()
    
