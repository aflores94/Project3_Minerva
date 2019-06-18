from django.urls import path 
from .views import teacher, student, parent, main

urlpatterns = [
    path('', main.home, name='home'),

    path('Students/home.html', student.login, name='login'),
    path('Students/index.html', student.index, name='student_index'),

    path('Teachers/home.html', teacher.login, name='login'),
    path('Teachers/index.html', teacher.index, name='teacher_index'),

    path('Parents/home.html', parent.login, name='login'),
    path('Parents/index.html', parent.index, name='parent_index'),
]


