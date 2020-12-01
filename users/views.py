from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views import generic
from . forms import CustomUserCreationForm, LoginForm, CandidateProfileForm, UserModelForm, ExaminerProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import CandidateProfile, ExaminerProfile, Candidate


# view for user sign up
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:signup_success')
    template_name = 'users/signup.html'

def SignUpSuccess(request):
    return render(request, 'users/signup_success.html')

# view for login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'users/welcome.html')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


# view to link users to specific profile update
@login_required
def user_profile(request):
    return render(request, 'users/edit_profile.html')

# log out
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/login/')

# views for candidates to update profile info
@login_required
@transaction.atomic
def candidate_edit_profile(request):
    if request.user.status == 'candidate':
        profile_form = CandidateProfileForm()
        status = request.user.status
        # user = request.user

        if request.method == 'POST':
            profile_form = CandidateProfileForm(
                instance=request.user.candidateprofile,
                data=request.POST,
                files=request.FILES
            )

            if profile_form.is_valid():
                profile_form.save(commit=True)
                #CandidateProfile.candidate = request.user.id
                #my_user.candidate = CandidateProfile.candidate
                #my_user.save()
                print('candidate profile added successfully')
                messages.success(request, 'Your profile has been updated successfully')

                context = {
                    'user': request.user,
                    'unique_id': request.user.unique_id,
                    'first_name': request.user.first_name,
                    'middle_name': profile_form.cleaned_data['middle_name'],
                    'last_name': request.user.last_name,
                    'username': request.user.username,
                    'status': request.user.status,
                    'gender': profile_form.cleaned_data['gender'],
                    'age': profile_form.cleaned_data['age'],
                    'address': profile_form.cleaned_data['address'],
                    'religion': profile_form.cleaned_data['religion'],
                    'phone': profile_form.cleaned_data['phone_number'],
                    'email': request.user.email,
                    'height': profile_form.cleaned_data['height'],
                    'hobbies': profile_form.cleaned_data['hobbies'],
                    'about_me': profile_form.cleaned_data['about_me'],
                }
                return render(request, 'users/candidate_profile_detail.html', context)
            else:
                print('candidate profile failed to add')
                messages.error(request, 'Update Profile Error')

        else:
            profile_form = CandidateProfileForm(instance=request.user.candidateprofile)
        return render(request, 'users/candidate_profile.html', {
            'profile_form': profile_form,
            'status': status
            # 'user': user
        })
    elif request.user.status == 'examiner':
        messages.error(request, 'Registration Failed!! Please register as an examiner')
        # profile_form = CandidateProfileForm()

    else:
        messages.error(request, 'Please register as either a candidate or an examiner')
        profile_form = CandidateProfileForm()

# view for examiners to update profile info
@login_required
@transaction.atomic
def examiner_edit_profile(request):
    if request.user.status == 'examiner':
        examiner_form = ExaminerProfileForm()
        # user = request.user

        if request.method == 'POST':
            examiner_form = ExaminerProfileForm(
                instance=request.user.examinerprofile,
                data=request.POST,
                files=request.FILES
            )

            if examiner_form.is_valid():
                examiner_form.save(commit=True)
                messages.success(request, 'Your profile has been updated successfully')

                context = {
                    'unique_id': request.user.unique_id,
                    'first_name': request.user.first_name,
                    'middle_name': examiner_form.cleaned_data['middle_name'],
                    'title': examiner_form.cleaned_data['title'],
                    'last_name': request.user.last_name,
                    'status': request.user.status,
                    'qualification': examiner_form.cleaned_data['qualification'],
                    'discipline': examiner_form.cleaned_data['discipline'],
                    'published_work': examiner_form.cleaned_data['published_work'],
                    'gender': examiner_form.cleaned_data['gender'],
                    'age': examiner_form.cleaned_data['age'],
                    'address': examiner_form.cleaned_data['address'],
                    'religion': examiner_form.cleaned_data['religion'],
                    'phone_num': examiner_form.cleaned_data['phone_number'],
                    'email': request.user.email,
                    'height': examiner_form.cleaned_data['height'],
                    'about_me': examiner_form.cleaned_data['about_me'],
                }
                return render(request, 'users/examiner_profile_detail.html', context)
            else:
                messages.error(request, 'Update Profile Error')
        else:
            examiner_form = ExaminerProfileForm(instance=request.user.examinerprofile)
        return render(request, 'users/examiner_profile.html', {
            'examiner_form': examiner_form,
            'status': request.user.status
            # 'user': user
        })
    elif request.user.status == 'candidate':
        messages.error(request, 'Registration Failed!! Please register as a candidate')
    else:
        messages.error(request, 'Please register as either a candidate or an examiner')


@login_required
def candidate_profile(request):
    if CandidateProfile.objects.filter(candidate=request.user).exists():    # not probably needed
        print(request.user, 'is available')
        x = CandidateProfile.objects.get(candidate=request.user)
        if x.middle_name is None:
            print('middle_name is null, add')
            messages.info(request, 'You have no profile yet. Add your profile details first.')
            return HttpResponseRedirect('/users/candidate_profile/')
        else:
            print('middle_name is available as ', x.middle_name)
            obj = CandidateProfile.objects.get(candidate=request.user)
            context = {
                'unique_id': request.user.unique_id,
                'username': request.user.username,
                'status': request.user.status,
                'middle_name': obj.middle_name,
                'gender': obj.gender,
                'dob': obj.date_of_birth,
                'age': obj.age,
                'address': obj.address,
                'religion': obj.religion,
                'phone_num': obj.phone_number,
                'email': request.user.email,
                'height': obj.height,
                'hobbies': obj.hobbies,
                'profile_pic': obj.profile_picture,
                'about_me': obj.about_me,

            }
            return render(request, 'users/candidate.html', context)

@login_required
def examiner_profile(request):
    if ExaminerProfile.objects.filter(examiner=request.user).exists():
        print(request.user, 'is available')
        x = ExaminerProfile.objects.get(examiner=request.user)
        if x.middle_name is None:
            print('middle_name is null, add')
            messages.info(request, 'You have no profile yet. Add your profile details first.')
            return HttpResponseRedirect('/users/examiner_profile/')
        else:
            print('middle_name is available as ', x.middle_name)
            print(request.user.id)
            obj = ExaminerProfile.objects.get(examiner=request.user)
            context = {
                'unique_id': request.user.unique_id,
                'username': request.user.username,
                'status': request.user.status,
                'title': obj.title,
                'middle_name': obj.middle_name,
                'qualification': obj.qualification,
                'discipline': obj.discipline,
                'published_work': obj.published_work,
                'gender': obj.gender,
                'dob': obj.date_of_birth,
                'age': obj.age,
                'address': obj.address,
                'religion': obj.religion,
                'phone_num': obj.phone_number,
                'email': request.user.email,
                'height': obj.height,
                # 'profile_pic': obj.profile_pic,
                'about_me': obj.about_me,

            }
            return render(request, 'users/examiner.html', context)


@login_required
def update_candidate(request):
    context = {}
    obj = get_object_or_404(CandidateProfile, id=request.user.id)
    form = CandidateProfileForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect('/users/candidate_detail/')
    context['form'] = form
    return render(request, 'users/update_candidate.html', context)

@login_required
def update_examiner(request):
    context = {}
    obj = get_object_or_404(ExaminerProfile, id=request.user.id)
    form = ExaminerProfileForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect('/users/examiner_detail/')
    context['form'] = form
    return render(request, 'users/update_examiner.html', context)
