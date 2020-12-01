from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from exams.models import Question, Department, StudentClass, StudentLevel, Subjects


def civic_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(examiner=request.user)
    stds_class = StudentClass.objects.filter(examiner=request.user)
    stds_level = StudentLevel.objects.filter(examiner=request.user)
    subjects = Subjects.objects.filter(examiner=request.user)

    return render(request, 'set_question/question.html', {
        'questions': questions,
        'examiner': examiner,
        'departments': departments,
        'stds_class': stds_class,
        'stds_level': stds_level,
        'subjects': subjects
    })


class CreateQue(View):
    def get(self, request):
        examiner_id = request.GET.get('examiner', None)
        print(examiner_id)
        examiner1 = get_user_model().objects.get(id=examiner_id)
        print(examiner1)

        department_id = request.GET.get('department', None)
        department1 = Department.objects.get(id=department_id)

        student_class_id = request.GET.get('student_class', None)
        student_class1 = StudentClass.objects.get(id=student_class_id)

        student_level_id = request.GET.get('student_level', None)
        student_level1 = StudentLevel.objects.get(id=student_level_id)

        subject_id = request.GET.get('subject', None)
        subject1 = Subjects.objects.get(id=subject_id)

        question1 = request.GET.get('question', None)
        option_A1 = request.GET.get('option_A', None)
        option_B1 = request.GET.get('option_B', None)
        option_C1 = request.GET.get('option_C', None)
        option_D1 = request.GET.get('option_D', None)
        correct_answer1 = request.GET.get('correct_answer', None)

        obj = Question.objects.create(
            examiner=examiner1,
            department=department1,
            student_class=student_class1,
            student_level=student_level1,
            subject=subject1,
            question=question1,
            option_A=option_A1,
            option_B=option_B1,
            option_C=option_C1,
            option_D=option_D1,
            answer=correct_answer1
        )

        question = {
            'id': obj.id,
            'examiner': obj.examiner,
            'department': obj.department,
            'student_class': obj.student_class,
            'student_level': obj.student_level,
            'subject': obj.subject,
            'question': obj.question,
            'option_A': obj.option_A,
            'option_B': obj.option_B,
            'option_C': obj.option_C,
            'option_D': obj.option_D,
            'answer': obj.answer
        }

        data = {
            'question': question
        }
        print(data)
        return JsonResponse(data)
