from django.db import models

# Create your models here.
from users.models import CustomUser


class StudentDepartment(models.Model):
    candidate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department


class StudentSubjects(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=25)
    subject_code = models.CharField(max_length=6)
    department = models.ForeignKey(StudentDepartment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject_name} ({self.subject_code}) by {self.candidate}'

class ClassStudent(models.Model):
    candidate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    student_class = models.CharField(max_length=20)

    def __str__(self):
        return self.student_class


class LevelStudent(models.Model):
    candidate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    student_level = models.CharField( max_length=20)

    def __str__(self):
        return self.student_level

