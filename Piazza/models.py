from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=32)
    email=models.CharField(max_length=64)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    course_desc=models.CharField(max_length=200)
    teacher=models.CharField(max_length=30,default="naresh")
    def __str__(self):
        return self.course_name
class post(models.Model):
    post_desc=models.CharField(max_length=150)
    post_details=models.CharField(max_length=1000)
    course=models.ForeignKey(Course)
    posted_by=models.ForeignKey(user)
    def __str__(self):
        return self.post_desc