from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	#context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html',context=context_dict)

def about(request):
	context_dict={'boldmessage':"Edima"}
	return render(request, 'rango/about.html',context=context_dict)

	#return HttpResponse("Rango says here is the about page! <br/> <a href='/rango/'>Main</a>.")