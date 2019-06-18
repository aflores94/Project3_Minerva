from django.urls import path 
from views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('accounts/login/', logout_view, name='login'),
    path('logout/', login_view, name='login'),
    path('home/', parent.home, name='parent_home'),
    path('home/', parent.home, name='parent_home'),
    path('home/', students.home, name='student_home'),
    path('home/', teachers.home, name='teacher_home'),

]