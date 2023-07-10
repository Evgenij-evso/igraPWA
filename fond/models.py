from django.db import models

class Form(models.Model):
    fio = models.CharField('ФИО',max_length=40)
    job_title = models.CharField('Работа', max_length=75)
    url_progect = models.URLField('Сылка на проект', max_length=250)
    summ = models.IntegerField('Деньги', max_length=7)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'Фонд форм'
        verbose_name_plural = 'Формы фонда'