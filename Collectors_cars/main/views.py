from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Task#, Post
from .forms import TaskForm#, PostForm
from django.contrib.auth import authenticate, login
from django.views import View, generic
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserCreationForm

def index(request):
    tasks = Task.objects.all()
    #posts = Post.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


#class PostListView(generic.ListView):
    #model = Post

#class PostDetailView(LoginRequiredMixin, generic.DetailView):
    #model = Post
def about(request):
    return render(request, 'main/about.html')



def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


#@login_required  1012
#@permission_required('blog.add_post', raise_exception=False)
#def create_post(request):
#    error = ''
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#        else:
#            error = 'Форма не верна'

#    form = PostForm()
#    context = {
#        'form': form,
#        'error': error
#    }
#    return render(request, 'main/create_post.html', context)

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

#def about(request):
#    return HttpResponse("<h4>about<h4>")
