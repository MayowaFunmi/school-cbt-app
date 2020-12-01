from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import CustomUser, CandidateProfile, ExaminerProfile
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# forms for custom user login
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('status', 'username', 'email', 'first_name', 'last_name')     # UserCreationForm.Meta.fields + ('unique_id',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('status', 'username', 'email', 'first_name', 'last_name')  # UserCreationForm.Meta.fields

# form for user login:
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# form for candidates to update profile

class UserModelForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('status', )

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        exclude = ['candidate', 'profile_date', 'candidate_id']

    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('middle_name', css_class='form-control'),
        Field('gender', css_class='form-control'),
        Field('date_of_birth', css_class='form-control'),
        Field('age', css_class='form-control'),
        Field('address', css_class='form-control'),
        Field('religion', css_class='form-control'),
        Field('phone_num', css_class='form-control'),
        Field('height', css_class='form-control'),
        Field('hobbies', css_class='form-control'),
        Field('about_me', css_class='form-control'),

    )

# view for examiners to update profile
class ExaminerProfileForm(forms.ModelForm):
    class Meta:
        model = ExaminerProfile
        exclude = ['examiner', 'profile_date']