from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'Registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('Teachers/home.html')
        elif request.user.is_student:
            return redirect('Students/index.html')
        else:
            return redirect('Parents/index.html')
    return render(request, 'home.html')


