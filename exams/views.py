from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.base import View

from students.models import StudentDepartment, ClassStudent, LevelStudent, StudentSubjects
from users.models import Examiner
from .models import Question, Score, Subjects, Department, StudentClass, StudentLevel, ExamRegistration
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

# views for ajax
from django.views import generic
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict


# view for students to register for exam
@login_required()
def register_exam(request):
    if request.user.status == 'candidate':
        candidate = get_user_model().objects.get(username=request.user)
        departments = Department.objects.all()
        student_class = StudentClass.objects.all()
        student_level = StudentLevel.objects.all()
        subjects = Subjects.objects.all()  # display subjects by departments

        if request.method == 'POST':
            candidate_id = request.POST.get('candidate')
            department_id = request.POST.get('department')
            student_class_id = request.POST.get('student_class')
            student_level_id = request.POST.get('student_level')
            subject_ids = request.POST.getlist('subject')

            student = get_user_model().objects.get(id=candidate_id)
            department = Department.objects.get(id=department_id)
            std_class = StudentClass.objects.get(id=student_class_id)
            std_level = StudentLevel.objects.get(id=student_level_id)

            sub_1_id = subject_ids[0]
            subject_1 = Subjects.objects.get(id=sub_1_id)

            sub_2_id = subject_ids[1]
            subject_2 = Subjects.objects.get(id=sub_2_id)

            sub_3_id = subject_ids[2]
            subject_3 = Subjects.objects.get(id=sub_3_id)

            sub_4_id = subject_ids[3]
            subject_4 = Subjects.objects.get(id=sub_4_id)

            sub_5_id = subject_ids[4]
            subject_5 = Subjects.objects.get(id=sub_5_id)

            sub_6_id = subject_ids[5]
            subject_6 = Subjects.objects.get(id=sub_6_id)

            sub_7_id = subject_ids[6]
            subject_7 = Subjects.objects.get(id=sub_7_id)

            sub_8_id = subject_ids[7]
            subject_8 = Subjects.objects.get(id=sub_8_id)

            sub_9_id = subject_ids[8]
            subject_9 = Subjects.objects.get(id=sub_9_id)
            try:
                reg = ExamRegistration(
                    candidate=student,
                    department=department,
                    student_class=std_class,
                    student_level=std_level,
                    subject_1=subject_1,
                    subject_2=subject_2,
                    subject_3=subject_3,
                    subject_4=subject_4,
                    subject_5=subject_5,
                    subject_6=subject_6,
                    subject_7=subject_7,
                    subject_8=subject_8,
                    subject_9=subject_9,
                )
                reg.save()

                context = {
                    'student': student,
                    'department': department,
                    'std_class': std_class,
                    'std_level': std_level,
                    'subject_1': subject_1,
                    'subject_2': subject_2,
                    'subject_3': subject_3,
                    'subject_4': subject_4,
                    'subject_5': subject_5,
                    'subject_6': subject_6,
                    'subject_7': subject_7,
                    'subject_8': subject_8,
                    'subject_9': subject_9,
                }
                messages.success(request, 'Exam Registration saved successfully')
                return render(request, 'exams/register_exam_success.html', context)

            except:
                messages.error(request, 'Exam Registration Failed')
                return render(request, 'exams/register_exam.html')

        return render(request, 'exams/register_exam.html', {
            'candidate': candidate,
            'departments': departments,
            'student_class': student_class,
            'student_level': student_level,
            'subjects': subjects
        })

    elif request.user.status == 'examiner':
        messages.error(request, 'You are not registered as a candidate!')
    else:
        messages.error(request, 'Please log in as either a candidate or an examiner')


'''
@login_required
def register_exam(request):
    if request.user.status == 'candidate':
        form = ExamRegistrationForm()
        # user = request.user

        if request.method == 'POST':
            form = ExamRegistrationForm(request.POST)

            if form.is_valid():
                my_user = form.save(commit=False)
                ExamRegistration.user = request.user.id
                my_user.user = ExamRegistration.user
                my_user.save()
                context = {
                    'user': request.user,
                    'subject_3': form.cleaned_data['subject_3'],
                    'subject_4': form.cleaned_data['subject_4'],
                    'subject_5': form.cleaned_data['subject_5'],
                    'subject_6': form.cleaned_data['subject_6'],
                    'subject_7': form.cleaned_data['subject_7'],
                    'subject_8': form.cleaned_data['subject_8'],
                    'subject_9': form.cleaned_data['subject_9'],
                }
                return render(request, 'exams/register_exam_success.html', context)

        return render(request, 'exams/register_exam.html', {
            'form': form,
            # 'user': user
        })

    elif request.user.status == 'examiner':
        messages.error(request, 'You are not registered as a candidate!')
    else:
        messages.error(request, 'Please log in as either a candidate or an examiner')


'''


def add_department(request):
    if request.user.is_staff:
        admin = get_user_model().objects.get(username=request.user)
        return render(request, 'exams/add_department.html', {'admin': admin})

    elif request.user.status == 'candidate':
        candidate = get_user_model().objects.get(username=request.user)
        return render(request, 'exams/add_department.html', {'candidate': candidate})


def add_department_save(request):
    if request.user.is_staff and request.method == 'POST':
        admin_id = request.POST.get('admin')
        admin = get_user_model().objects.get(id=admin_id)
        department = request.POST.get('department_name')

        try:
            dept = Department(admin=admin, department=department)
            dept.save()
            messages.success(request, "Successfully Added Department")
            return HttpResponseRedirect('/exams/add_department/')
        except:
            messages.error(request, "Failed to Add Department")
            return HttpResponseRedirect('/exams/add_department/')

    elif request.user.status == 'candidate' and request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        candidate = get_user_model().objects.get(id=candidate_id)
        department = request.POST.get('department_name')

        try:
            dept = StudentDepartment(candidate=candidate, department=department)
            dept.save()
            messages.success(request, "Successfully Added Department")
            return HttpResponseRedirect('/exams/add_department/')
        except:
            messages.error(request, "Failed to Add Department")
            return HttpResponseRedirect('/exams/add_department/')

    else:
        messages.error(request, "Method Not Allowed")
        return HttpResponseRedirect('/exams/add_department/')


def edit_department(request):
    admin = get_user_model().objects.get(username=request.user)
    depts = Department.objects.all()
    return render(request, 'exams/edit_department.html', {'depts': depts, 'admin': admin})


def edit_department_save(request):
    if request.method == 'POST':
        admin_id = request.POST.get('examiner')
        department_id = request.POST.get('department')

        examiner = get_user_model().objects.get(id=admin_id)
        department = Department.objects.get(id=department_id)

        try:
            dept = Department.objects.get(id=admin_id)
            dept.department = department
            dept.save()
            messages.success(request, "Successfully Edited Department")
            return HttpResponseRedirect('/exams/edit_department')
        except:
            messages.error(request, "Failed to Edit Department")
            return HttpResponseRedirect('/exams/edit_department')
    else:
        messages.error(request, "Method Not Allowed")
        return HttpResponseRedirect('/exams/edit_department')


@login_required
def add_subject(request):
    if request.user.is_staff:
        admin = get_user_model().objects.get(username=request.user)
        depts = Department.objects.all()

        return render(request, 'exams/add_subject.html', {'admin': admin, 'depts': depts})
    elif request.user.status == 'candidate':
        candidate = get_user_model().objects.get(username=request.user)
        depts = Department.objects.all()

        return render(request, 'exams/add_subject.html', {'candidate': candidate, 'depts': depts})


def add_subject_save(request):
    if request.user.is_staff and request.method == 'POST':
        admin_id = request.POST.get('admin')
        admin = get_user_model().objects.get(id=admin_id)
        subject_name = request.POST.get('subject_name')
        subject_code = request.POST.get('subject_code')
        department_id = request.POST.get('department')
        department = Department.objects.get(id=department_id)

        try:
            subject_add = Subjects(admin=admin, subject_name=subject_name, subject_code=subject_code,
                                   department=department)
            subject_add.save()
            messages.success(request, "Successfully Added Subject")
            return HttpResponseRedirect('/exams/add_subject/')
        except:
            messages.error(request, "Failed to Add Subject")
            return HttpResponseRedirect('/exams/add_subject/')

    elif request.user.status == 'candidate' and request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        candidate = get_user_model().objects.get(id=candidate_id)
        subject_name = request.POST.get('subject_name')
        subject_code = request.POST.get('subject_code')
        department_id = request.POST.get('department')
        department = Department.objects.get(id=department_id)

        try:
            subject_add = StudentSubjects(candidate=candidate, subject_name=subject_name, subject_code=subject_code,
                                          department=department)
            subject_add.save()
            messages.success(request, "Successfully Added Subject")
            return HttpResponseRedirect('/exams/add_subject/')
        except:
            messages.error(request, "Failed to Add Subject")
            return HttpResponseRedirect('/exams/add_subject/')

    else:
        messages.error(request, "Method Not Allowed")
        return HttpResponseRedirect('/exams/add_subject/')


@login_required
def add_student_class(request):
    if request.user.is_staff:
        admin = get_user_model().objects.get(username=request.user)
        return render(request, 'exams/add_student_class.html', {'admin': admin})

    elif request.user.status == 'candidate':
        candidate = get_user_model().objects.get(username=request.user)
        return render(request, 'exams/add_student_class.html', {'candidate': candidate})


@login_required
def add_student_class_save(request):
    if request.user.is_staff and request.method == 'POST':
        admin_id = request.POST.get('admin')
        admin = get_user_model().objects.get(id=admin_id)
        student_class = request.POST.get('student_class')

        try:
            stud_class = StudentClass(admin=admin, student_class=student_class)
            stud_class.save()
            messages.success(request, "Successfully Added Student Class")
            return HttpResponseRedirect('/exams/add_student_class/')
        except:
            messages.error(request, "Failed to Add Student Class")
            return HttpResponseRedirect('/exams/add_student_class/')

    elif request.user.status == 'candidate' and request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        candidate = get_user_model().objects.get(id=candidate_id)
        student_class = request.POST.get('student_class')

        try:
            stud_class = StudentClass(candidate=candidate, student_class=student_class)
            stud_class.save()
            messages.success(request, "Successfully Added Student Class")
            return HttpResponseRedirect('/exams/add_student_class/')
        except:
            messages.error(request, "Failed to Add Student Class")
            return HttpResponseRedirect('/exams/add_student_class/')

    else:
        messages.error(request, "Method Not Allowed")
        return HttpResponseRedirect('/exams/add_student_class/')


@login_required
def add_student_level(request):
    if request.user.is_staff:
        admin = get_user_model().objects.get(username=request.user)
        return render(request, 'exams/add_student_level.html', {'admin': admin})

    elif request.user.status == 'candidate':
        candidate = get_user_model().objects.get(username=request.user)
        return render(request, 'exams/add_student_level.html', {'candidate': candidate})


@login_required
def add_student_level_save(request):
    if request.user.is_staff and request.method == 'POST':
        admin_id = request.POST.get('admin')
        admin = get_user_model().objects.get(id=admin_id)
        student_level = request.POST.get('student_level')

        try:
            stud_level = StudentLevel(admin=admin, student_level=student_level)
            stud_level.save()
            messages.success(request, "Successfully Added Student Level")
            return HttpResponseRedirect('/exams/add_student_level/')
        except:
            messages.error(request, "Failed to Add Student Level")
            return HttpResponseRedirect('/exams/add_student_level/')

    elif request.user.status == 'candidate' and request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        candidate = get_user_model().objects.get(id=candidate_id)
        student_level = request.POST.get('student_level')

        try:
            stud_level = LevelStudent(candidate=candidate, student_level=student_level)
            stud_level.save()
            messages.success(request, "Successfully Added Student Level")
            return HttpResponseRedirect('/exams/add_student_level/')
        except:
            messages.error(request, "Failed to Add Student Level")
            return HttpResponseRedirect('/exams/add_student_level/')

    else:
        messages.error(request, "Method Not Allowed")
        return HttpResponseRedirect('/exams/add_student_level/')


# view for teachers to set question
@login_required
def exam_question(request):
    if request.user.status == 'examiner':
        form = QuestionForm()
        # user = request.user

        context = {
            'form': form,
            # 'user': user
        }

        if request.method == 'POST':
            form = QuestionForm(request.POST)

            if form.is_valid():
                my_user = form.save(commit=False)
                my_user.user = request.user
                my_user.save()

                return render(request, 'exams/question_summary.html', {
                    'exam': Question.objects.order_by('pk'),
                    'question': form.cleaned_data['question'],
                    'A': form.cleaned_data['A'],
                    'B': form.cleaned_data['B'],
                    'C': form.cleaned_data['C'],
                    'D': form.cleaned_data['D'],
                    'answer': form.cleaned_data['answer'],
                })
        return render(request, 'exams/set_question.html', context)
    elif request.user.status == 'candidate':
        messages.error(request, 'You are not registered as an examiner')


# for students to answer questions
score = 0


@login_required
def student_answer(request):
    if request.user.status == 'candidate':
        form = AnswerForm()
        all_questions = Question.objects.order_by('pk')
        paginator = Paginator(all_questions, 1)
        page = request.GET.get('page')
        questions = paginator.get_page(page)
        global score

        if request.method == 'POST':
            form = AnswerForm(request.POST)

            if form.is_valid():
                messages.success(request, 'Your Answer has been submitted')

                for question in questions:
                    cor_ans = question.answer
                    std_ans = form.cleaned_data['your_answer']

                    if std_ans == cor_ans:
                        score += 1
                print(score)

                # return render(request, 'exams/score.html', {'score': score})'

        return render(request, 'exams/question.html', {  # student_answer.html
            'form': form,
            'questions': questions,
            'score': score
        })
    elif request.user.status == 'examiner':
        messages.error(request, 'You are not registered as a candidate')


########################## Start Ajax Views ####################################
# display the question page
def set_ajax_question(request):
    questions = Question.objects.order_by('pk')
    # add subject class data to question html page
    return render(request, 'exams/ajax_exams/exam_question.html', {'questions': questions})


'''
class AjaxQuestion(ListView):
    model = Question
    template_name = 'exams/ajax_exams/exam_question.html'
    context_object_name = 'questions'
'''


# views for examiners to set questions using ajax(CreateView)

class CreateQuestion(View):
    def get(self, request):
        question1 = request.GET.get('question', None)
        option_A1 = request.GET.get('option_A', None)
        option_B1 = request.GET.get('option_B', None)
        option_C1 = request.GET.get('option_C', None)
        option_D1 = request.GET.get('option_D', None)
        correct_answer1 = request.GET.get('correct_answer', None)

        obj = Question.objects.create(
            question=question1,
            option_A=option_A1,
            option_B=option_B1,
            option_C=option_C1,
            option_D=option_D1,
            answer=correct_answer1
        )

        question = {
            'id': obj.id,
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


# Update Question
class UpdateQuestion(View):
    def get(self, request, id):
        question1 = request.GET.get('question', None)
        option_A1 = request.GET.get('option_A', None)
        option_B1 = request.GET.get('option_B', None)
        option_C1 = request.GET.get('option_C', None)
        option_D1 = request.GET.get('option_D', None)
        correct_answer1 = request.GET.get('correct_answer', None)

        obj = Question.objects.get(pk=id)
        obj.question = question1
        obj.option_A = option_A1
        obj.option_B = option_B1
        obj.option_C = option_C1
        obj.option_D = option_D1
        obj.answer = correct_answer1
        obj.save()

        question = {
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
        return JsonResponse(data)


########################## End Ajax Views ####################################

# views to exams by subjects and classes/level

@login_required
def accounts_ss1(request):
    questions = Question.objects.order_by('pk')
    return render(request, 'exams/account/account_ss1.txt', {'questions': questions})


# @login_required
class CreateAccountSS1Question(View):
    def get(self, request):
        question1 = request.GET.get('question', None)
        option_A1 = request.GET.get('option_A', None)
        option_B1 = request.GET.get('option_B', None)
        option_C1 = request.GET.get('option_C', None)
        option_D1 = request.GET.get('option_D', None)
        correct_answer1 = request.GET.get('correct_answer', None)
        # sub = Subjects.objects.get(subject_code='CEC100')
        # que = Question(subject=sub.subject)
        # que.save(commit=False)

        obj = Question.objects.create(
            question=question1,
            option_A=option_A1,
            option_B=option_B1,
            option_C=option_C1,
            option_D=option_D1,
            answer=correct_answer1
        )

        question = {
            'id': obj.id,
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


# view for question with radio select button
def answer(request):
    all_questions = Question.objects.order_by('pk')
    paginator = Paginator(all_questions, 1)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'exams/question.html', {'questions': questions})