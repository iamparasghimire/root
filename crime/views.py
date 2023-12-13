from django.shortcuts import render, redirect
from .forms import CrimeForm
from .models import Crime

def index(request):
    form = CrimeForm()

    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after successful form submission

    return render(request, 'crime/index.html', {'form': form})
