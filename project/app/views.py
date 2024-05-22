from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import CreateView
from .models import Statment
from .forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class= RegistrationForm
    success_url = reverse_lazy('login')

@login_required
def allStatment(request):
    statments = Statment.objects.filter(user=request.user)
    return render(request, 'statment/allStatment.html', {"statments": statments})

@login_required
def CreateStatment(request):
    if request.method == 'POST':
        statment = Statment()
        statment.user = request.user
        statment.title = request.POST.get('title')
        statment.description = request.POST.get('description')
        statment.set_time = request.POST.get('set_time')
        statment.save()
        return redirect('allStatment')
    return render(request, 'statment/createStatment.html')