from student_app.models import *
from django import forms 

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = "__all__"