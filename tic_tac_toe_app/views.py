#views.py
from tic_tac_toe_app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import random
import simplejson

def to_str(key, value):
    if isinstance(key, unicode):
        key = int(key)
    if isinstance(value, unicode):
        value = str(value)
    return key, value

def game(request, id=33):
	id = request.GET.get('id')

	
	request.session['error'] = ""
	if id == 33 or  id == None:

		data = {
		0: "",
		1: "",
		2: "",
		10: "",
		11: "",
		12: "",
		20: "",
		21: "",
		22: ""
		}
		request.session['name'] ='sreenath';
		data1 = {}
		for item in sorted(data):
			print type(item)
			data1[item] = data[item]
		
		data = data1
		print data
		request.session['game_data'] = data

	else:
		data = request.session['game_data']
		print data
		id = int(id)
		
		data2 = {}
		for d in data:
			k, l = to_str(d, data[d])
			data2[k] = l

		data1 = {}
		for item in data2:
			# item = int(item)
			# print type(item), item
			string = ""
			if data2.get(item):
				string = data2.get(item, '')
				print 'hi'
			# print string + "string is" + data[id]
			
			data1[item] = string
		
		data = data1
		
		if data[id] != "":
			request.session['error'] = "already choosen"
			return render_to_response('game.html',context_instance=RequestContext(request))
		print 'else'
		data[id] = "X"
		# data1={}
		# for item in sorted(data):
		# 	data1[item] = data[item]
		# data = data1
		print data
		x = id / 10
		y = id % 10
		print x,y
		# status = gameStatus(data, "X", x, y)
		# if status == "won":
		# 	winner = "X"
		# while True:
		# 	x,y = get_random(data)
		# 	if data[int(x +''+y)] == "":
		# 		print 'null red' 
		request.session['game_data'] = data
	return render_to_response('game.html',context_instance=RequestContext(request))
 
def get_random(data):
	x = random.randint(0,2)
	y = random.randint(0,2)

	return x, y


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):

	for key in request.session.keys():
		del request.session[key]
	# logout(request)
	return render_to_response('registration/logout.html',)
	# return HttpResponseRedirect('/')

def mygame(request):
	
	data1 = request.GET.get("current_state")

	coords = request.GET.get("coords")
	coords = int(eval(coords))
	m = coords / 10
	n = coords % 10
	# print m, n
	# print coords
	data = eval(data1)
	# print data
	user = ""

	status = gameStatus(data, "X", m, n)
	if status == "won":
		user = "X"
	count = 0
	while True:
		x = random.randint(0,2)
		y = random.randint(0,2)
		if status == "won":
				user = "X"
				break
		if data[x][y] == "" or data[x][y] == None:
			# print x, y
			data[x][y] = "O"
			
			
			status1 = gameStatus(data, "O", x, y)
			if status != "won" and status1 == "won":
				user = "O"
				status = status1
			break
		count += 1
		if count > 18 and status != "won" :
			status = "draw"
			break
	# print simplejson.dumps(data)
	# data = simplejson.dumps(data)
	# print user, status
	return HttpResponse(simplejson.dumps({'data1':data, 'status':status, 'user':user}))

def gameStatus(board, ch, row, column):
	place1 = 0
	place2 = 0
	status = None
    
	if column == row :
		if board[0][0] == ch and board[1][1] == ch and board[2][2] == ch:
			place1 = 1;
      
	if column + row == 2:
		if board[0][2] == ch and board[1][1] == ch and board[2][0] == ch:
			place2 = 1;

	if (board[row][0] == ch and board[row][1] == ch and board[row][2] == ch) or (board[0][column] == ch and board[1][column] == ch and board[2][column] == ch) or (place2 == 1 or place1 == 1):
		status = "won";

	return status;

 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )