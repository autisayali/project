from django.http import HttpResponse
from Home.models import Entry
from Home.models import Task
from django.template import loader

from django.shortcuts import render,HttpResponse,HttpResponseRedirect



# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        if Entry.objects.filter(uname=uname):
            return render(request,'todo.html')
        else:
            return render(request,'todo.html')

    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def features(request):
    return render(request,'features.html')

def signup(request):

    if request.method=='POST':
       uname=request.POST.get('uname')
       email=request.POST['email']
       password=request.POST['password']
       
       entry=Entry(uname=uname,email=email,password=password).save()
       
       return render(request,'login.html') 
    
    return render(request,'signup.html')

def send(request):
    if request.method=='POST':
        taskdate=request.POST['taskdate']
        desc=request.POST['desc']
        priority=request.POST['priority']
        complete=request.POST['complete']
        assign=request.POST['assign']
        
        print(taskdate,desc,priority,complete,assign)

        Task(taskdate=taskdate,desc=desc,assign=assign,priority=priority,complete=complete).save()
      
    
    data=Task.objects.all()
    
   
    
    return render(request,'todo.html',{'data':data})
    

def todo(request):
  
    return render(request,'todo.html')

def addtask(request):
    
    return render(request,'addtask.html')

def show(request):
   
    data=Task.objects.all()
    
    print(data)
    return render(request,'show.html',{'data': data})

def get(request):
    taskdate=request.GET['taskdate']
    desc=request.GET['desc']
    priority=request.GET['priority']
    complete=request.GET['complete']
    Task(taskdate=taskdate,desc=desc,priority=priority,complete=complete).objects.save()
    return render(request,'show.html')


def edit(request):
    id = request.GET['id']
    taskdate = desc = priority=complete="Not Available"
    for data in Task.objects.filter(id=id):
        taskdate = data.taskdate
        desc = data.desc
        assign=data.assign
        priority=data.priority
        complete=data.complete
    return render(request,"edit.html",{'id':id,'taskdate':taskdate,'desc':desc,'assign':assign,'priority':priority,'complete':complete})
 




def RecordEdited(request):
    if request.method == 'POST':
        id = request.POST['id']
        taskdate = request.POST['taskdate']
        desc = request.POST['desc']
        assign=request.POST['assign']
        priority=request.POST['priority']
        complete=request.POST['complete']
        Task.objects.filter(id=id).update(taskdate=taskdate,desc=desc,assign=assign,priority=priority,complete=complete)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

def delete_task(request):
    id = request.GET['id']
    Task.objects.filter(id=id).delete()
    return HttpResponseRedirect("show")





def complete(request): 
    data = Task.objects.filter(complete='Yes').values()
  
    context = {
        'data': data,
    }
    
    
    return render(request,"complete.html",{'data':data})

    
def priority(request):
  data = Task.objects.filter(priority='High').values()
  
  context = {
    'data': data,
  }
  return render(request,"priority.html",{'data':data})