from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
# Create your views here.

def home_page(request):
    if request.method=="GET":
        return render(request,'index.html',)

def contact(request):
    if request.method=="POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        message_name=firstname +" "+ lastname
        #      message_email=request.POST['email']
        #      message=request.POST['message']
        #      print(message_name)
        #      pass
        global mes
        mes = {'mes': message_name}
        subject = "Subject : " + request.POST['subject']
        msg = "Message : " + request.POST['message']
        to = request.POST['email']
        msg = subject + " \n" + msg + " \n Contact Me !" + to
        send_mail(message_name, msg,to,['princesingwal@gmail.com'])
        print(request.POST)
        return redirect('home_page',)

