from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserCreationForm, CustomUserChangeForm
from . models import CustomUser, Candidate, Examiner, CandidateProfile, ExaminerProfile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'unique_id', 'status', 'first_name', 'last_name']
    list_filter = ['status']
    search_fields = ('status',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Candidate)
admin.site.register(CandidateProfile)
admin.site.register(Examiner)
admin.site.register(ExaminerProfile)