from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from forms import PersonForm
from models import Person, Image

from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'key': "value" })

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class UpdatePersonView(UpdateView):
	queryset = Person.objects.all()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class ListPersonView(ListView):
	model = Person
	template_name='person_list.html'

def Gallery(request):
	image_list = Image.objects.all().order_by('?')[:259]
	session_list = Session.objects.all()

	# request.session['x'] = request.session.get('x',0) + 1
	# messages="x: %s"%( request.session['x'] )
	return render(request, 'my_gallery.html', {'image_list': image_list,'session_list': session_list })

def Sessions(request,num="1"):
	number = num

	i = len(Person.objects.all()) 					# always new user
	i=i+14
	obj = Person.objects.get(pk=i).pk				# get pk from Person
	listdb = request.session.get("key",[obj])

	if obj == obj:
		listdb.append(number)

	request.session["key"] = listdb

	if len(listdb)==8:
		request.session.set_expiry(10)

	for i in Session.objects.all():
		print SessionStore().decode(i.session_data)

	return render(request, 'image.html', {'image_show': Image.objects.get(id=number),'listdb': listdb,'user_id': obj })

def Clear(request):
	try:
		# del request.session["key"]
		request.session.flush()
	except KeyError:
		pass
	return redirect('person')