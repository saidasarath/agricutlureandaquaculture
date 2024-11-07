import datetime
import requests
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.http import HttpResponse
import re
from .models import *
from django.core.mail import send_mail
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'index.html')
def hon(request):
    return render(request,'index.html')
def times(request):
    var1=datetime.datetime.now()
    data=datetime1(time12=var1)
    data.save()
    return HttpResponse(var1)
def weather3(request):
    return render(request,'weather.html')
def weather2(request):
    if request.method=='POST':

        place = request.POST.get('cityname')
        api_key = 'fbdcb3297c21556bdbaf6445e3d56559'

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={place}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            print("No City Found")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            # °C = [(°F-32)×5] / 9
            temp1 = (((temp - 32) * 5) / 9)
            # print(type(temp))
        return HttpResponse(
            f"The weather {place}  is: {weather}\nThe temperature{place} is: {temp}ºF\nThe temperature in {place} is: {temp1}ºC")
def qrocode2(request):
    return render(request,'qrcode1.html')
import qrcode
from django.http import FileResponse
def qrcode12(request):
    if request.method=='POST':
        sid=request.POST.get('sid')
        sname=request.POST.get('sname')
        data1=sid+sname
        qr=qrcode.QRCode(version=1,box_size=30,border=5)
        qr.add_data(data1)
        qr.make(fit=True)
        img=qr.make_image(fill_color='black',back_color='white')
        img.save('static/KLU.png')
        img1=open('static/KLU.png','rb')
        response=FileResponse(img1)
        return response
    else:
        return HttpResponse("not working")
@login_required(login_url='/login')
def contactus1(request):
    return render(request,"contactus.html")
def contactus3(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend = comment + '\n-------------------------------------thank you for the comment___________________________________'
        data = contactus(firstname=firstname, lastname=lastname,email=email,comment=comment)
        data.save()
        send_mail(
            'Thank you for contacting HLI syatem',
            tosend,
            'kakumanusaidasarath@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>mail sent</center></h1>")
    else:
        HttpResponse("<h1>error</h2>")
def registerpage(request):
    return render(request,"register.html")
def registerpage1(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        email=request.POST['email']
        phonenumber = request.POST['phonenumber']
        # data = register(username=username,password=password, email=email, phonenumber=phonenumber)
        # data.save()
        if len(username)==0:
            return render(request, "error.html")
        if len(password)==0:
            return render(request,"passerror.html")
        if len(phonenumber)!=10 and phonenumber.isnumeric()==False:
            return render(request,"error.html")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern,email):
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('/login')
        else:
            return render(request,"error.html")
    else:
        render(request,"error.html")
@login_required(login_url='/login')
def about(request):
    return render(request,"about.html")
def login(request):
    return render(request,"login.html")
def login1(request):
    if request.method=="POST":
        username = request.POST["email"]
        password = request.POST["password"]

        user=auth.authenticate(username=username,password=password)
        if username=='admin' and password=='12345':
            auth.login(request, user)
            return render(request,"adminnav.html")
        elif user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('/login')
    else:
        return HttpResponse("<font color=red>Login Failed</font>")
@login_required(login_url='/login')
def purchase(request):
    products=Product.objects.all()
    data={
        'products':products
    }
    return render(request,"purchase.html",data)

def deatils(request):
    return render(request,"details.html")
def adminabout(request):
    return render(request, "adminabout.html")
def adminhome(request):
    return render(request, "adminhome.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

