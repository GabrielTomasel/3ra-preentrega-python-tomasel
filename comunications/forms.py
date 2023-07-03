from django import forms

class CourseForm(forms.Form):
    course_id = forms.IntegerField()
    course_type = forms.CharField()

