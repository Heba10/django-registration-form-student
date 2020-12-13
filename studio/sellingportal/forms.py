from django import forms

class Registar(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    age = forms.CharField()
    date_birth = forms.CharField()

class DegreeRegistar(forms.Form):
    student_degree = forms.CharField(label='student_degree', max_length=100)
