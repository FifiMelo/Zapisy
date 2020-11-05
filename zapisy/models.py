from django.db import models

# Create your models here.

class Termin(models.Model):
    language = models.CharField(max_length=10)
    teacher_name = models.CharField(max_length=15)
    teacher_surename = models.CharField(max_length=15)
    date = models.CharField(max_length=10)
    hour = models.CharField(max_length=5)
    available = models.BooleanField(default=True)
    

class Uczen(models.Model):
    name = models.CharField(max_length=15)
    surename = models.CharField(max_length=15)
    passcode = models.CharField(max_length=8)
    polski = models.ForeignKey(Termin, on_delete=models.SET_NULL, blank=True, null=True,related_name='+')
    obcy = models.ForeignKey(Termin, on_delete=models.SET_NULL, blank=True, null=True,related_name='+')
    polish_teacher = models.CharField(max_length=31)
    english_teacher = models.CharField(max_length=31)
    foreign_teacher = models.CharField(max_length=31)
    


