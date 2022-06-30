from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
# from myapp.forms import todoform
from myapp.models import Todo
from users.models import Account


# Create your views here.

def todo(request):

    return render(request,"home.html")
    
def delete(request):
    if request.method=='GET':
        pk= request.GET['t_id']
        obj = Todo.objects.get(id = pk)
        obj.delete()

        return JsonResponse({'status':'deleted'})

def add_todos(request):
    if request.method == 'GET':
        task = request.GET['task']
        userid = request.GET['uid']
        
        user_obj = Account.objects.get(id=userid)
        Todo.objects.create(user = user_obj, task = task)
        
        latest = Todo.objects.filter(user=user_obj).order_by('-id')[0]
        my_task = latest.get_json()

        return JsonResponse({'status':1,'latest':my_task}, safe=False)

def get_all(request):
    if request.method =='GET':
        user_id = request.GET['id']
        uobj = Account.objects.get(id=user_id)
        all_todos = list(Todo.objects.filter(user = uobj).values())

        # print(all_todos)
        return JsonResponse({'all_todos':all_todos})
