from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    if request.method =="POST":
        error = ''
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')             # после действии перекидывает на указыный адрес
        else:
            error = "Форма было неверной"
    form    = TaskForm()
    context = {
        'form': form 
    }
    return render(request, 'main/create.html', context)
