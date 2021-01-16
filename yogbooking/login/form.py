from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Very Basic Example of a Django Form

class Userregister(UserCreationForm):
    email = forms.EmailField(required=True)
    fathers_name = forms.CharField(max_length = 50)
    aadhar = forms.IntegerField()
    address = forms.CharField(max_length=20)
    city = forms.CharField(max_length=50)
    profile = forms.ImageField()
    proffession = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=12)
	
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
   def clean_message(self):
       username = self.cleaned_data.get("username")
       dbuser = Dreamreal.objects.filter(name = username)
       if not dbuser:
           raise forms.ValidationError("User does not exist in our db!")
       return username