from __future__ import annotations
from django.db import models


    
class Student(models.Model):
    name = models.CharField("the person's name",max_length=100)   
    birth_date = models.DateField() 
    
    def __str__(self):
        return self.name    
    
class Test(models.Model):
    subject = models.CharField(max_length=100)
    grade = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject   