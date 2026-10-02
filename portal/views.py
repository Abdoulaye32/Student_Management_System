from django.shortcuts import render


def dashboard(request):
    return render(request, 'portal/index.html')


def students(request):
    return render(request, 'portal/students.html')

def add_student(request):
    return render(request, 'portal/add-student.html')

def academic_records(request):
    return render(request, 'portal/academic-records.html')


def courses(request):
    return render(request, 'portal/courses.html')


def settings(request):
    return render(request, 'portal/settings.html')


def logout(request):
    return render(request, 'portal/logout.html')
