from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    major = models.CharField(max_length=200)

    def __str__(self):
        return self.name