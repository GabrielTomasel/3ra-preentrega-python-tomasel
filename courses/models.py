from django.db import models

class Course(models.Model):
    course_id = models.IntegerField(6)
    course_type = models.CharField(max_length=25)