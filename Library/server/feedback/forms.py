from django import forms
from django.forms import Textarea

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
#        exclude = []
        fields = ['customer_name', 'email', 'details', 'book', 'happy',]
        widgets = {
            'details': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            ),
            'email': Textarea(
                attrs={
                    'placeholder': 'Введтие ваш email формата name@example.ru'
                }
            )
        }
