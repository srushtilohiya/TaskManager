from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.core.mail import send_mail
from django.conf import settings
from tasks.utils import send_invitations 
from django.http import HttpResponse

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description, user=request.user)
        return redirect('index')
    return render(request, 'tasks/create_task.html')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('index')
    return render(request, 'tasks/edit_task.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('index')

@login_required
def invite_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = "You're Invited to Join the Task Manager App!"
        message = "Click the link to join: http://localhost:8000/accounts/signup/"
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
        return redirect('index')
    return render(request, 'tasks/invite_user.html')


 # Import the send_invitations function

def send_invitations_view(request):
    send_invitations()  # This sends invitations to all emails in the AdminInvite model
    return HttpResponse("Invitations sent successfully!")