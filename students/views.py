from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages

# student question view
from exams.models import ExamRegistration, Department, StudentClass, StudentLevel, Subjects, Question

# view for candidate to select exam subject to write
def select_subject(request):
    # add view to reject subject not registered by candidate
    return render(request, 'students/select_subject.html')

# not needed anymore
def get_question(request):
    candidate = ExamRegistration.objects.filter(candidate=request.user)

    if request.method == 'POST':
        department_id = request.POST.get('department')
        student_class_id = request.POST.get('student_class')
        student_level_id = request.POST.get('student_level')
        subject_id = request.POST.get('subject')

        department = Department.objects.get(id=department_id)
        student_class = StudentClass.objects.get(id=student_class_id)
        student_level = StudentLevel.objects.get(id=student_level_id)
        subject = Subjects.objects.get(id=subject_id)

        all_questions = Question.objects.filter(department=department, student_class=student_class, student_level=student_level, subject=subject).order_by('pk')
        paginator = Paginator(all_questions, 1)
        page = request.GET.get('page')
        questions = paginator.get_page(page)
        return render(request, 'students/questions.html', {'questions': questions})

    return render(request, 'students/get_question.html', {'candidate': candidate})


score = 0
def question(request):
    candidate = ExamRegistration.objects.get(candidate=request.user)
    subject_list = []
    subject_list.append(candidate.subject_1.id)
    subject_list.append(candidate.subject_2.id)
    subject_list.append(candidate.subject_3.id)
    subject_list.append(candidate.subject_4.id)
    subject_list.append(candidate.subject_5.id)
    subject_list.append(candidate.subject_6.id)
    subject_list.append(candidate.subject_7.id)
    subject_list.append(candidate.subject_8.id)
    subject_list.append(candidate.subject_9.id)

    maths = Subjects.objects.filter(subject_name='Mathematics', subject_code='MTH101')

    for m in maths:
        num = m.id
        if num in subject_list:
            all_questions = Question.objects.filter(subject=num).order_by('pk')
            paginator = Paginator(all_questions, 1)
            page = request.GET.get('page')
            questions = paginator.get_page(page)
            global score

            if request.method == 'POST':
                cor_ans = request.POST.get('answer')
                std_ans = request.POST.get('question')
                print(cor_ans)
                print(std_ans)

                if std_ans == cor_ans:
                    score += 1
                else:
                    print('no')
            print(score)
            return render(request, 'students/questions.html', {'questions': questions})
        else:
            messages.error(request, 'You did not register for this subject!!!')
            return render(request, 'students/questions.html')
