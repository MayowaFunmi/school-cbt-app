from django import forms
from .models import Question

# form for candidates to register for an exam
'''
class ExamRegistrationForm(forms.ModelForm):
    class Meta:
        model = ExamRegistration
        exclude = ['user', 'register_date']

'''

# form for examiners to set questions
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['date']

 # form for students to answer questions
class AnswerForm(forms.Form):
    your_answer = forms.CharField(max_length=1)
'''
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer' ]
'''