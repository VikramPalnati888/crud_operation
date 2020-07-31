from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
import pytz
from SBAV_App.models import *
from SBAV_App.forms import *


def login(request):
	if request.method == "POST":
		username, password = request.POST['username'], request.POST['password']
		user = authenticate(request,username=username, password=password)
		if user:
			auth_login(request,user)
			user_name = request.user
			return redirect('items_get')
		else:
			messages.error(request, 'Invalid Login Credentials')
			return redirect('login')
	else:
		user_name = request.user
		return render(request, 'login.html', {'user': user_name})


def Logout(request):
	logout(request)
	return redirect('login')

@login_required
def ItemsPost(request):
	if request.method == "POST":
		Items.objects.create(Item_Name= request.POST['Item_Name'],
								Item_Cost=int(request.POST['Item_Cost']),
								Items_In_Stock=int(request.POST['Items_In_Stock']))
		return redirect('items_get')
	return render(request, 'items_post.html', {'message':"data stored successful"})

@login_required
def itemsGet(request):
	if request.method == "GET":
		data = {}
		data_list = []
		items_qs = Items.objects.all().order_by('-id')
		for dt in items_qs:
			data[dt.id] = {
							"Item_Id": dt.id,
							"Item_Name": dt.Item_Name,
							"Items_In_Stock": int(dt.Items_In_Stock),
							"Items_Out_Stock": int(dt.Items_Out_Stock),
							"Item_Cost":dt.Item_Cost,
							"Created_at": dt.Created_at.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d"),
							}
		data_list.append(data)
		return render(request, 'items_get.html', {'response':data_list})

@login_required
def itemsEdit(request, pk):
	items_data = Items.objects.get(id=pk)
	if request.method == 'POST':
		item_obj = Items.objects.get(id = pk)
		item_obj.Item_Name = request.POST['Item_Name']
		item_obj.Item_Cost = request.POST['Item_Cost']
		item_obj.Items_In_Stock = int(request.POST['Items_In_Stock']) - int(request.POST['Items_Out_Stock'])
		item_obj.Items_Out_Stock = request.POST['Items_Out_Stock']
		item_obj.save()
		return redirect('items_get')
	return render(request, "items_edit.html", {'data':items_data})

@login_required
def itemsDelete(request,pk):
	item_obj = Items.objects.get(id=pk)
	item_obj.delete()
	return redirect("items_get")