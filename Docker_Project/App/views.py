from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')  # Redirect to the home page or any other page
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})
