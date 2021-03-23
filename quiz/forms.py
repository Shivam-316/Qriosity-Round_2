from django import forms
class AnswerForm(forms.Form):
    answer=forms.CharField(max_length=200)

class TimeForm(forms.Form):
    time = forms.IntegerField(min_value=0)