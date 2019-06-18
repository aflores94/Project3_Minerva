from django.urls import path 
from .views import teacher, student, parent, main

urlpatterns = [
    path('', main.home, name='home'),

    path('Students/home/', student.login, name='login'),
    path('Students/index/', student.index, name='student_index'),

    path('Teachers/home/', teacher.login, name='login'),
    path('Teachers/index/', teacher.index, name='teacher_index'),

    path('Parents/home/', parent.login, name='login'),
    path('Parents/index/', parent.index, name='parent_index'),
]


