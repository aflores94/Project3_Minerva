from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..forms import ParentSignUpForm
from ..models import Parent, User



