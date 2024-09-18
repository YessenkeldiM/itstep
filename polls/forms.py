from django import forms
from .models import Question
from captcha.fields import CaptchaField

class QuestionForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Question
        fields = '__all__'
        


class QuestionSearchForm(forms.Form):
    keyword = forms.CharField(max_length=20)
    question = forms.ModelChoiceField(queryset=Question.objects.all())

searchFactory = forms.formset_factory(QuestionSearchForm, extra=3)