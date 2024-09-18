from django.contrib import admin
from .models import Good, Magazin, MagazineGoods, Review

# Register your models here.
admin.site.register(Good)
admin.site.register(Magazin)
admin.site.register(MagazineGoods)
admin.site.register(Review)