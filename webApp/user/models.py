from django.db import models

# Create your models here.
class Yword(models.Model):
    eng = models.CharField('eng', max_length=40)
    ru = models.CharField('eng', max_length=40)

    def __str__(self):
        return f"{self.id}. {self.eng} - {self.ru}"

class Lesson(models.Model):
    name = models.CharField('name', max_length=40)
    description = models.CharField('description', max_length=150)
    yword = models.ManyToManyField(Yword)

    def __str__(self):
        return f"{self.id}. {self.name}"
    pass
