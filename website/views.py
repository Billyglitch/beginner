from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def contact(request):
    if request.method =="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']

        #send mail
        send_mail(
            fname,#subject
            message,#message
            email,#from
            ['jkopulunos@gmail.com','kingcool001@gmail.com'], #To
            )

        return render(request, 'appointment.html', {'fname':fname})

    else:
        return render(request, 'contact.html',{})

def about(request):
    return render(request, 'about.html',{})

def services(request):
    return render(request, 'services.html',{})

def appointment(request):
    if request.method == "POST":
        return render(request, 'appointment.html',{})
    else:
        return render(request, 'contact.html',{})

