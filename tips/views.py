from urllib import request
from django.shortcuts import render
from django.views import generic
from . forms import UserCreateForm, LoginForm
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_list_or_404
from . import models
from . forms import TopicForm, CommentForm



# Create your views here.

#スレッド作成ビュー
def create(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/top/')
        else:
            params['form'] = form
    else:
        params['form'] = TopicForm()
    return render(request, 'new_thread.html', params)

# Create your views here.


#ホームページ用ビュー
class HomeView(generic.TemplateView):
    template_name = "home.html"
    
#ルール表示ビュー
class RuleView(generic.TemplateView):
    template_name = "rule.html"
    
#トップページ表示ビュー
class TopView(ListView):
    model = models.Topic
    
    context_object_name = "topic_list"
    
    template_name = "top.html"


#アカウント作成ビュー
class Create_account(CreateView):
    def post(self, request,*args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            return redirect('/top/')
        return render(request, 'create.html', {'form': form,})
    
    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'create.html', {'form': form,})

create_account  = Create_account.as_view()
    
#ログインビュー
class Account_login(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            return redirect('/top/')
        return render(request, 'login.html', {'form': form})
    
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})
    
account_login = Account_login.as_view()


#各スレッド
def detail(request, pk):
    thread = get_object_or_404(models.Topic, pk=pk)
    
    context = {
        "thread": thread,
        "comments": models.Comment.objects.filter(target=thread.id)
    }
    return render(request, 'thread.html', context)

#コメント作成ビュー
class Comment(CreateView):
    template_name = 'comment.html'
    model = models.Comment
    form_class = CommentForm
    
    def form_valid(self,form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(models.Topic, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect("../", pk=post_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context