from django.urls import path
from . import views

urlpatterns = [
    # Django URLs
    path('', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('add-student/', views.add_student, name='add_student'),
    path('academic-records/', views.academic_records, name='academic_records'),
    path('courses/', views.courses, name='courses'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout, name='logout'),

    # Original HTML URLs
    path('students.html', views.students),
    path('add-student.html', views.add_student),
    path('academic-records.html', views.academic_records),
    path('courses.html', views.courses),
    path('settings.html', views.settings),
    path('logout.html', views.logout),
]
