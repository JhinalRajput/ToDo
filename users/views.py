from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Account
# Create your views here.

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email_id = request.POST['email_id']
        password = request.POST['password']

        if Account.objects.filter(username = username).exists():
            return JsonResponse({'status':'exist'})
        else:
            Account.objects.create(username = username, email_id=email_id, password = password)
            return JsonResponse({'status':'success'})
    return render(request, "signup.html")

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        if Account.objects.filter(username = username).exists():
            obj = Account.objects.get(username = username)
            obj_id = obj.id
            if obj.password == password:
                print("success")
                return JsonResponse({'id':obj_id})

def logout(request):
    return redirect('/')

def error(request):
    return render(request,"error.html")