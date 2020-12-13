from django.db import models

# Create your models here.
class Student(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	age=models.IntegerField(default=15)
	date_birth=models.DateTimeField()
	def __str__(self):
		return self.first_name

class Degree(models.Model):
	student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
	student_degree=models.IntegerField(default=15)
			
