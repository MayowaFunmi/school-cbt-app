from django.shortcuts import render


def home(request):
    return render(request, 'landing/base1.html')

def about(request):
    return render(request, 'landing/general/about.html')

def contact(request):
    return render(request, 'landing/general/contacts.html')

def instruction(request):
    return render(request, 'landing/general/instructions.html')

def members(request):
    return render(request, 'landing/general/members.html')

def exam_details(request):
    return render(request, 'landing/general/details.html')

