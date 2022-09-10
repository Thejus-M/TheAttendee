from django.db import models


class student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    class_section = models.CharField(max_length=10)

class Class(models.Model):
    class Meta:
        verbose_name = "class" 
        verbose_name_plural = "classes" 
    classname = models.CharField(max_length=10,primary_key=True)
    student = models.ManyToManyField(student)
    def name(self):
        return self.student.name
    
    def __str__(self):
        return f'{self.classname}'
    
class Attendant(models.Model):
    student = models.ForeignKey(student, on_delete=models.DO_NOTHING)
    attendants = models.BooleanField(default=False)
    subject = models.CharField(max_length=10)
    period_no = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    
    def name(self):
        return self.student.name
