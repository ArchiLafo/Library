from django.db import models

class Feedback(models.Model):
    customer_name = models.CharField(max_length=120, verbose_name='Ваше ФИО')
    email = models.EmailField(verbose_name='Ваш почтовый адрес')
    details = models.TextField(verbose_name='Ваш вопрос')
    book = models.TextField(max_length=120, verbose_name='Название книги')
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name