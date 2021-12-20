from django.db import models


class StudentDetails(models.Model):
    Student_Name = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Marks = models.IntegerField(default=0)
