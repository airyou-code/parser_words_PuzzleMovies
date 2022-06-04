from django.db import models

class Word(models.Model):
    eng = models.CharField('eng', max_length=40)
    ru = models.CharField('ru', max_length=40)
    description = models.CharField('description', max_length=150)
    dateTime = models.DateTimeField('dateTime', auto_now=True)

    def __str__(self):
        return f"{self.id}. {self.eng} - {self.ru}"
