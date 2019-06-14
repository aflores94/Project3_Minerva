from django.urls import path 
from views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', login, name='login'),
    path('login/', logout_view, name='login'),
    path('logout/', login_view, name='login'),
]