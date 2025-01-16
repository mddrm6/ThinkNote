from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Note
from .forms import NewNoteForm, EditNoteForm

def detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    return render(request, 'detail.html', {
        'note': note
    })

@login_required
def notes_list(request):
    notes = Note.objects.filter(created_by=request.user)

    return render(request, 'notes.html', {
        'notes': notes
    })

@login_required
def new_note(request):
    if request.method == 'POST':
        form = NewNoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()

            return redirect('note:notes_list')
    else:
        form = NewNoteForm()

    return render(request, 'note_form.html', {
        'form': form,
        "title": 'New note',
    })

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()

            return redirect('note:notes_list')
    else:
        form = EditNoteForm(instance=note)

    return render(request, 'note_form.html', {
        'form': form,
        'note': note,
        "title": 'Edit note',
    })

@login_required
def delete(request, pk):
    note = get_object_or_404(Note, pk=pk, created_by=request.user)
    note.delete()

    return redirect('note:notes_list')
