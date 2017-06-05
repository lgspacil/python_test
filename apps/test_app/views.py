import bcrypt
from django.shortcuts import render, redirect
from .models import User, Item
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def index(request):
	return render(request, 'test_app/index.html')


def login(request):

	#passing in info to postData
	postData = {
		'email' : request.POST['email'],
		'password' : request.POST['password']
	}

	model_rep = User.objects.login_check(postData)
	

	if model_rep[0] and model_rep[1] == True:
		#store the user who is logged in information in a session
		request.session['first_name'] = model_rep[2]
		request.session['last_name'] = model_rep[3]
		request.session['id'] = model_rep[4]
		messages.success(request, model_rep[5][0])
		return redirect('/success')
	elif model_rep[0] == True and model_rep[1] == False:
		messages.error(request, "Invalid Password")
	else:
		messages.error(request, "Invalid Email")

	return redirect('/')

	


def register(request):

	postData = {
	'first_name': request.POST['first_name'],
	'last_name': request.POST['last_name'],
	'email' : request.POST['email'],
	'password' : request.POST['password'],
	'confirm_password' : request.POST['confirm'],
	}
	
	model_rep = User.objects.register_check(postData)

	if model_rep[0] == False:
		print model_rep[1][0]
		messages.error(request, model_rep[1][0])
		return redirect('/')
	else:
		request.session['first_name'] = model_rep[1]
		request.session['last_name'] = model_rep[2]
		request.session['id'] = model_rep[3]
		messages.success(request, model_rep[4][0])
		return redirect('/success')

def success(request):

	context = {
	'other_items': Item.objects.exclude(users=request.session['id']),
	'all_items': Item.objects.all(),
	'currentuser': User.objects.get(id=request.session['id']),

	}

	return render(request, 'test_app/success.html', context)


def create_item_page(request, id):

	return render(request, 'test_app/create.html')

def add_item(request):

	newest_item = Item.objects.filter(item_name=request.POST['item'])

	if len(newest_item) != 0:
		messages.error(request, "This item already exists")
		return render(request, 'test_app/create.html')
	else:
		user = User.objects.get(id=request.session['id'])
		new_item = Item.objects.create(users=user, item_name=request.POST['item'])

		new_item.adders.add(user)

	return redirect('/success')

def delete_item(request, id):

	this_item = Item.objects.get(id=id)
	this_item.delete()
	return redirect('/success')

def add_your_list(request, id):
	#the id is the items id
	one = 1
	other_item = Item.objects.get(id=id)
	user = User.objects.get(id=request.session['id'])

	other_item.adders.add(user)

	other_item.number = one
	other_item.save()


	return redirect('/success')
	#return render(request, 'test_app/success.html', context)

def remove_wish_list(request, id):
	zero = 0
	other_item = Item.objects.get(id=id)
	user = User.objects.get(id=request.session['id'])

	other_item.adders.remove(user)

	other_item.number = zero
	other_item.save()

	return redirect('/success')


def item_detail(request, id):
	#id is item id
	all_users = Item.objects.filter(id=id)
	all_users = all_users[0].adders.all()
	print all_users

	context = {
	'items':Item.objects.filter(id=id),
	'allusers':all_users,
	}

	# print context['users'][0].adders.all()

	return render(request, 'test_app/item_detail.html', context)

def money(request):
	return render(request, 'test_app/money.html')
