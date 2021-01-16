from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout,login,authenticate
from django.views.decorators.csrf import csrf_exempt, csrf_protect
#from login.form import Instructorregister
from login.form import LoginForm,Userregister
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "loginapp.html",
                    context={"form":form})
#def register(request):
 #   instructor = Instructorregister()
  #  return render(request,'register.html',{'instructor' : instructor})

def logout_view(request):
    logout(request)
    return redirect('/')
        #user=Instructor(name,fathers_name,aadhar,mobile,dob,email,joblocation,qualification,address,experiance,city,resume,profile,pic1,pic2,pic3,pic4)
        #user.save()
       # return redirect('loginapp')
    #else:
        #return render(request,'register.html')


    #return render(request,'register.html')
def registerstudent(request):
    return render(request,'regstudent.html')

def register(request):
	if request.method == "POST":
		form = Userregister(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/login")
		#messages.error(request, "Unsuccessful registration. Invalid information.")
	form = Userregister
	return render (request=request, template_name="register.html", context={"register_form":form})

