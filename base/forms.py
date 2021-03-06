#coding:utf_8
from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm  

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'username'}))
    #first_name = forms.CharField(required = False)
    #last_name = forms.CharField(required = False)
    #birtday = forms.DateField(required = False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        #user.first_name = self.cleaned_data['first_name']
        #user.last_name = self.cleaned_data['last_name']
        #user.birthday = self.cleaned_data['birthday']

        if commit:
            user.save()

        return user