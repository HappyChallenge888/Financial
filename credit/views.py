from django.shortcuts import render

# Create your views here.
def index(request):
	template = 'credit/index.html'
	context = {}
	return render(request, template, context)

def create(request):
	template = 'credit/create.html'
	context = {}
	return render(request, template, context)

def detail(request, pk):
	template = 'credit/create.html'
	context = {}
	return render(request, template, context)

def finish(request):
	template = 'credit/finish.html'
	context = {}
	return render(request, template, context)