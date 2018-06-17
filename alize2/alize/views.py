from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Pizza,Category,Steak,Salad,Comment
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms
from .forms import CommentForm


def index(request):
    return render(request,'main/index.html')

def reg(request):
    return render(request,'main/reg.html')

def pizza(request):

    pizza_by_id = Pizza.objects.all()
    context = {
    	'pizzas' : pizza_by_id, 
    }
    return render(request,'main/items.html',context)
    
def category(request):

	category_by_id = Category.objects.all()
	context = {
		'categories' : category_by_id,
	}
	return render(request,'main/menu.html',context)

def about(request):
    return render(request,'main/about.html')

def contact(request):
	comment_by_id = Comment.objects.all()
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.save()
			return redirect('contact')
	else:
		form = CommentForm()
	context = {
		'comments' : comment_by_id,
		'form' : form,
	}
	return render(request, 'main/contact.html', context)

def steak(request):

	steak_by_id = Steak.objects.all()
	context = {
		'steaks' : steak_by_id,
	}
	return render(request,'main/items.html',context)
    
def salad(request):

	salad_by_id = Salad.objects.all()
	context = {
		'salads' : salad_by_id,
	}
	return render(request,'main/items.html',context)



def login(request):
	args={}
	args.update(csrf(request))
	
	if request.POST:
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		user=auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('user')
		else:
			args['login_error']="No such username"
			return render_to_response('main/login.html', args)
	else:
		return render_to_response('main/login.html', args)

def logout(request):
	auth.logout(request)
	return redirect("/")

def reg(request):
	args={}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			
			newuser = auth.authenticate(Username=newuser_form.cleaned_data['username'],Password=newuser_form.cleaned_data['password2'])
			newuser_form.save()
			auth.login(request, newuser)
			return redirect('/')
		else:
			args['form']=newuser_form
	return render_to_response('main/reg.html', args)



def user(request):
	return render(request, 'main/user.html')

def edit(request):
	if request.POST:
		form = UserChangeForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('user')

	else:
		form = UserChangeForm(instance=request.user)
		args = {'form': form}
		return render(request,'main/edit.html',args)


def teacher(request):
	return render(request,'main/teacher.html')
# Create your views here.


