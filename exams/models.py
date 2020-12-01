from django.db import models
from users.models import Candidate, Examiner, CustomUser
# Create your models here.

DEPARTMENT = [
        ('General', 'General Studies'),
        ('Science', 'Science Class'),
        ('Commercial', 'Commercial Class'),
        ('Arts', 'Arts Class'),
    ]

SUBJECTLIST = [
        ('Civic', 'Civic Education'),
        ('Marketing', 'Marketing'),
        ('Econs', 'Economics'),
        ('Bio', 'Biology'),
        ('Agric', 'Agricultural Science'),
        ('Govt', 'Government'),
        ('Yor', 'Yoruba Language'),
        ('Acc', 'Financial Accounting'),
        ('Geo', 'Geography'),
        ('Chem', 'Chemistry'),
        ('Further Maths', 'Further Mathematics'),
        ('Comm', 'Commerce'),
        ('CRS', 'Christian Religious Knowledge'),
        ('Lit', 'Literature In English'),
        ('Phy', 'Physics'),
    ]

CANDIDATECLASS = [
        ('JSS', 'Junior Secondary'),
        ('SSS', 'Senior Secondary'),
    ]

CANDIDATELEVEL = [
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
    ]

class Department(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=25)
    subject_code = models.CharField(max_length=6)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject_name} ({self.subject_code}) by {self.admin}'

class StudentClass(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    student_class = models.CharField(choices=CANDIDATELEVEL, max_length=20)

    def __str__(self):
        return self.student_class


class StudentLevel(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    student_level = models.CharField(choices=CANDIDATELEVEL, max_length=20)

    def __str__(self):
        return self.student_level

# models to set exam questions
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    examiner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    student_level = models.ForeignKey(StudentLevel, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, null=True)
    question = models.TextField(max_length=1000)
    option_A = models.CharField(max_length=1000)
    option_B = models.CharField(max_length=1000)
    option_C = models.CharField(max_length=1000)
    option_D = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-question']

    def __str__(self):
        return self.question


class Answer(models.Model):
    candidate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=1000)
    answer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'({self.candidate.last_name} {self.candidate.first_name}) {self.question} {self.question.answer}'

class Score(models.Model):
    score = models.CharField(max_length=6)

    def __str__(self):
        return self.score

# model for student to register for exams
class ExamRegistration(models.Model):
    candidate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, help_text='Select the department you belong to', on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    student_level = models.ForeignKey(StudentLevel, on_delete=models.CASCADE)
    subject_1 = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_1', blank=True, null=True)
    subject_2 = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_2', blank=True, null=True)
    subject_3 = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_3', blank=True, null=True)
    subject_4 = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_4', blank=True, null=True)
    subject_5 = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_5', blank=True, null=True)
    subject_6 = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_6', blank=True, null=True)
    subject_7 = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_7', blank=True, null=True)
    subject_8 = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_8', blank=True, null=True)
    subject_9 = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_9', blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.candidate.last_name} {self.candidate.first_name} ({self.candidate.unique_id})'


class ExaminerExamRegistration(models.Model):
    examiner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    student_level = models.ForeignKey(StudentLevel, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.examiner.last_name} {self.examiner.first_name} ({self.examiner.unique_id})'
