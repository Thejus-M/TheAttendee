from django.db import models


class student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    class_section = models.CharField(max_length=10)

class Attendant(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    attendants = models.BooleanField()
    subject = models.CharField(max_length=10)
    period_no = models.IntegerField()
    time = models.DateTimeField(auto_now=True)