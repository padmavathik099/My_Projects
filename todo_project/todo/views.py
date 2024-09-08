from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ToDoItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Todo
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')  # Redirect to a success page or your to-do list
            else:
                return render(request, 'todo/login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'todo/login.html', {'error': 'Username and password are required'})
    return render(request, 'todo/login.html')


@login_required
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})


@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user  # Get the currently logged-in user

        todo = Todo.objects.create(
            user=user,  # Assign the logged-in user to the todo
            title=title,
            description=description,
            completed=False
        )
        return redirect('todo_list')




def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'todo/signup.html', {'error': 'Username already exists'})
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('login')
        else:
            return render(request, 'todo/signup.html', {'error': 'Passwords do not match'})
    return render(request, 'todo/signup.html')




def update_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    action = request.GET.get('action')
    if action == 'mark_completed':
        todo.completed = True
    elif action == 'mark_pending':
        todo.completed = False
    todo.save()
    return redirect('todo_list')

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')

def home(request):
    return render(request, 'todo/home.html')

from django.shortcuts import render, redirect
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Assign the current user to the todo item
            todo.save()
            return redirect('todo_list')  # Redirect to the todo list page after saving
    else:
        form = TodoForm()

    return render(request, 'todo/add_todo.html', {'form': form})



