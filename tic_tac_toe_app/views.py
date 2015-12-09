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