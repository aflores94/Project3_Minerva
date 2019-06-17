from django.urls import path 
from views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('accounts/login/', logout_view, name='login'),
    path('logout/', login_view, name='login'),
]git