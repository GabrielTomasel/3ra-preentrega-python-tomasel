from django.db import models
    
class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    
class Professor(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(null=True, default=None)
    
class Course(models.Model):
    course_id = models.IntegerField(6)
    course_type = models.CharField(max_length=25)
    
class Project(models.Model):
    course_id = models.IntegerField(6)
    task = models.CharField(max_length=25)
    expire_date = models.DateTimeField()
    
class User(models.Model) :
        first_name = models.CharField(max_length=25)
        last_name = models.CharField(max_length=25)
        email = models.EmailField()
        username = models.CharField(max_length=25)
        password = models.CharField(max_length=25)

