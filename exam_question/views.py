from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

from exams.models import Question, Department, StudentClass, StudentLevel, Subjects

def choose_exam(request):
    return render(request, 'exam_question/choose_exam.html')

def check_question(request):
    return render(request, 'exam_question/check_question.html')


def edit_question(request, question_id):
    question = Question.objects.get(id=question_id)
    examiner = get_user_model().objects.get(username=request.user)

    if request.method == 'POST':
        question = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('answer')

        q = Question.objects.get(id=question_id)
        q.question = question
        q.option_A = option_A
        q.option_B = option_B
        q.option_C = option_C
        q.option_D = option_D
        q.answer = answer
        q.save()

        questions = Question.objects.filter(examiner=request.user).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Edited Question")
        return render(request, 'exam_question/edit_question.html')
    else:
        messages.error(request, "Failed to Edit Question")

    return render(request, 'exam_question/edit_question.html', {'question': question, 'examiner': examiner, 'id': question_id })

# financial accounts question

def accounts_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Commercial Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Financial Accounting') #add subject_code

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/account/account_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/account/account_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


def accounts_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Commercial Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Financial Accounting')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/account/account_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/account/account_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


def accounts_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Commercial Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Financial Accounting')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/account/account_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/account/account_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


# Agric Science exams

def agric_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Agricultural Science')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/agric_sc/agric_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/agric_sc/agric_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


def agric_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Agricultural Science')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/agric_sc/agric_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/agric_sc/agric_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


def agric_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Agricultural Science')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/agric_sc/agric_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/agric_sc/agric_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# biology exams

def biology_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Biology')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/biology/biology_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/biology/biology_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def biology_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Biology')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/biology/biology_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/biology/biology_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def biology_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Biology')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/biology/biology_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/biology/biology_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# chemistry exams

def chemistry_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Chemistry')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/chemistry/chemistry_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/chemistry/chemistry_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def chemistry_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Chemistry')


    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/chemistry/chemistry_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/chemistry/chemistry_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def chemistry_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Chemistry')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/chemistry/chemistry_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/chemistry/chemistry_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# civic exams
def civic_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Civic Education')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/civic/civic_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/civic/civic_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def civic_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Civic Education')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/civic/civic_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/civic/civic_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def civic_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Civic Education')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/civic/civic_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/civic/civic_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


# commerce exams

def commerce_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Commercial Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Commerce')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/commerce/commerce_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/commerce/commerce_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def commerce_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Commercial Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Commerce')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/commerce/commerce_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/commerce/commerce_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def commerce_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Commercial Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Commerce')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/commerce/commerce_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/commerce/commerce_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# crs exams

def crs_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Christian Religious Studies')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/crs/crs_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/crs/crs_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def crs_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Christian Religious Studies')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/crs/crs_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/crs/crs_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def crs_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Christian Religious Studies')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/crs/crs_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/crs/crs_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# economics exams

def economics_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Economics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/economics/econs_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/economics/economics_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def economics_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Economics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/economics/econs_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/economics/economics_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


def economics_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Economics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/economics/econs_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/economics/economics_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# English Literature exams

def eng_literature_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Literature In English')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/eng_literature/lit_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/eng_literature/eng_literature_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def eng_literature_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Literature In English')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/eng_literature/lit_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/eng_literature/eng_literature_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def eng_literature_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Literature In English')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/eng_literature/lit_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/eng_literature/eng_literature_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# English Language exams

def english_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='English Language')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/english/english_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/english/english_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


def english_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='English Language')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/english/english_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/english/english_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


def english_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='English Language')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/english/english_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/english/english_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# Further Mathematics exams

def further_maths_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Further Mathematics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/further_maths/f_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/further_maths/further_maths_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def further_maths_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Further Mathematics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/further_maths/f_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/further_maths/further_maths_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def further_maths_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Further Mathematics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/further_maths/f_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/further_maths/further_maths_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# geography exams

def geography_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Geography')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/geography/geo_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/geography/geography_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def geography_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Geography')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/geography/geo_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/geography/geography_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def geography_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Geography')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/geography/geo_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/geography/geography_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


# government exams
def government_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Government')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/government/government_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/government/government_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def government_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Government')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/government/government_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/government/government_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def government_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Arts and Humanities')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Government')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/government/government_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/government/government_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# marketing exams

def marketing_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Marketing')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/marketing/marketing_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/marketing/marketing_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def marketing_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Marketing')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/marketing/marketing_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/marketing/marketing_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def marketing_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Marketing')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/marketing/marketing_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/marketing/marketing_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


# mathematics exams

def maths_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Mathematics', subject_code=101)

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/maths/maths_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/maths/maths_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


def edit_question(request, question_id):
    question = Question.objects.get(id=question_id)
    examiner = get_user_model().objects.get(username=request.user)

    if request.method == 'POST':
        question = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('answer')

        q = Question.objects.get(id=question_id)
        q.question = question
        q.option_A = option_A
        q.option_B = option_B
        q.option_C = option_C
        q.option_D = option_D
        q.answer = answer
        q.save()

        questions = Question.objects.filter(examiner=request.user).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Edited Question")
        return render(request, 'exam_question/test_summary.html', context)
    else:
        messages.error(request, "Failed to Edit Question")

    return render(request, 'exam_question/edit_question.html', {'question': question, 'examiner': examiner, 'id': question_id })



def maths_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Mathematics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/maths/maths_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/maths/maths_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def maths_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Mathematics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/maths/maths_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/maths/maths_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

# physics exams

def physics_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Physics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/physics/physics_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/physics/physics_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def physics_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='Science Class')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Physics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/physics/physics_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/physics/physics_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def physics_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter()
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Physics')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/physics/physics_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/physics/physics_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


# Yoruba Language exams

def yoruba_ss1(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=1)
    subjects = Subjects.objects.filter(subject_name='Yoruba Language')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/yoruba/yoruba_1_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/yoruba/yoruba_ss1.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')

def yoruba_ss2(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=2)
    subjects = Subjects.objects.filter(subject_name='Yoruba Language')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/yoruba/yoruba_2_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/yoruba/yoruba_ss2.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')


def yoruba_ss3(request):
    examiner = get_user_model().objects.get(username=request.user)
    questions = Question.objects.filter(examiner=request.user).order_by('pk')
    departments = Department.objects.filter(department='General Studies')
    stds_class = StudentClass.objects.filter(student_class='SSS')
    stds_level = StudentLevel.objects.filter(student_level=3)
    subjects = Subjects.objects.filter(subject_name='Yoruba Language')

    if request.method == 'POST':
        examiner_id = request.POST.get('examiner')
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')
        question  = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        answer = request.POST.get('correct_answer')

        examiner = get_user_model().objects.get(id=examiner_id)
        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        question_add = Question(examiner=examiner,
                                department=department,
                                student_class=student_class,
                                student_level=student_level,
                                subject=subject,
                                question=question,
                                option_A=option_A,
                                option_B=option_B,
                                option_C=option_C,
                                option_D=option_D,
                                answer=answer
                                )
        question_add.save()
        questions = Question.objects.filter(examiner=request.user, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        context = {
            'questions': questions
        }
        messages.success(request, "Successfully Added Question")
        return render(request, 'exam_question/question/yoruba/yoruba_3_summary.html', context)

    if stds_class and stds_level and subjects and departments:
        return render(request, 'exam_question/question/yoruba/yoruba_ss3.html', {
            'questions': questions,
            'examiner': examiner,
            'departments': departments,
            'stds_class': stds_class,
            'stds_level': stds_level,
            'subjects': subjects
        })
    else:
        messages.error(request, "You Cannot Add This Question!!!")
        return render(request, 'exam_question/choose_exam.html')
