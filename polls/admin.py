from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Question, Choice, Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Person ,PersonAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'question_text','comment', 'pub_date', 'my_name')
    list_editable = ('question_text', 'comment')
    search_fields = ('comment',)
    fields = ('question_text', )

    def my_name(self, obj):
        return 'Miras ' + str(obj)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        q =  super().get_queryset(request)
        return q
    

# Register your models here.
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
