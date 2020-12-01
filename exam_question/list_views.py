from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render

from exams.models import Question, Department, Subjects, StudentClass, StudentLevel, ExaminerExamRegistration


def list_questions(request):
    examiner = ExaminerExamRegistration.objects.filter(examiner=request.user)
    # departments = Department.objects.filter(admin=request.user)
    # subjects = Subjects.objects.filter(admin=request.user)
    # student_class = StudentClass.objects.filter(admin=request.user)
    # student_level = StudentLevel.objects.filter(admin=request.user)

    if request.method == 'POST':
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')

        department = Department.objects.get(id=department_id)
        std_class = StudentClass.objects.get(id=student_class_id)
        std_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        questions = Question.objects.filter(examiner=request.user, department=department, student_class=std_class, student_level=std_level, subject=subject).order_by('pk')
        nums = [i for i in range(1, 50)]
        return render(request, 'exam_question/question_details.html', {
            'questions': questions,
            'department': department,
            'subject': subject,
            'std_class': std_class,
            'std_level': std_level,
            'nums': nums
        })

    return render(request, 'exam_question/list_questions.html', {'examiner': examiner})


def examiner_exam_reg(request):
    examiner = get_user_model().objects.get(username=request.user)
    departments = Department.objects.all()
    subjects = Subjects.objects.all()
    stds_class = StudentClass.objects.all()
    stds_level = StudentLevel.objects.all()

    if request.method == 'POST':
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')

        try:
            examiner = get_user_model().objects.get(username=request.user)
            department = Department.objects.get(id=department_id)
            std_class = StudentClass.objects.get(id=student_class_id)
            std_level = StudentLevel.objects.get(id=student_level_id)
            subject = Subjects.objects.get(id=subject_id)

            reg = ExaminerExamRegistration(examiner=examiner, department=department, student_class=std_class, student_level=std_level, subject=subject)
            reg.save()

            examiner = get_user_model().objects.get(username=request.user)
            departments = Department.objects.all()
            subjects = Subjects.objects.all()
            stds_class = StudentClass.objects.all()
            stds_level = StudentLevel.objects.all()

            context = {
                'departments': departments,
                'subjects': subjects,
                'stds_class': stds_class,
                'stds_level': stds_level,
                'examiner': examiner
            }

            messages.success(request, 'Exam Registration saved successfully')
            return render(request, 'exam_question/question/examiner_exam_reg.html', context)
        except:
            messages.error(request, 'Exam Registration Failed')
            return render(request, 'exam_question/question/examiner_exam_reg.html')

    return render(request, 'exam_question/question/examiner_exam_reg.html', {
        'departments': departments,
        'subjects': subjects,
        'stds_class': stds_class,
        'stds_level': stds_level,
        'examiner': examiner
    })


def examiner_details(request):
    examiner = get_user_model().objects.get(username=request.user)
    details = ExaminerExamRegistration.objects.filter(examiner=request.user)

    return render(request, 'exam_question/examiner_details.html', {
        'examiner': examiner,
        'details': details
    })
