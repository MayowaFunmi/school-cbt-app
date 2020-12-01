from django.contrib import admin
from .models import StudentDepartment, StudentSubjects, ClassStudent, LevelStudent
# Register your models here.
admin.site.register(StudentDepartment)
admin.site.register(StudentSubjects)
admin.site.register(ClassStudent)
admin.site.register(LevelStudent)