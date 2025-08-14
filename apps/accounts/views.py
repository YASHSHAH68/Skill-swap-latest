from django.shortcuts import render , redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

