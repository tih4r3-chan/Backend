from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponse


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/cuenta/login/')
    else:
        form = RegistrationForm()
    return render(request, 'registro.html', {'form': form})
