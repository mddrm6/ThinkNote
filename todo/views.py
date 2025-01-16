from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Todo
from .forms import NewTodoForm, EditTodoForm

def detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    return render(request, 'detail.html', {
        'todo': todo
    })

@login_required
def todos_list(request):
    todos = Todo.objects.filter(created_by=request.user)

    return render(request, 'todos.html', {
        'todos': todos
    })

@login_required
def new_todo(request):
    if request.method == 'POST':
        form = NewTodoForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_by = request.user
            todo.save()

            return redirect('todo:todos_list')
    else:
        form = NewTodoForm()

    return render(request, 'todo_form.html', {
        'form': form,
        "title": 'New todo',
    })

@login_required
def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditTodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()

            return redirect('todo:todos_list')
    else:
        form = EditTodoForm(instance=todo)

    return render(request, 'todo_form.html', {
        'form': form,
        'todo': todo,
        "title": 'Edit todo',
    })

@login_required
def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, created_by=request.user)
    todo.delete()

    return redirect('todo:todos_list')

