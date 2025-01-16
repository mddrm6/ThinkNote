from django.shortcuts import render, redirect

from note.models import Note

from .forms import SignupForm

def index (request):
    notes = Note.objects.all()
    return render(request, 'index.html', {
        'notes': notes,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form,
    })
