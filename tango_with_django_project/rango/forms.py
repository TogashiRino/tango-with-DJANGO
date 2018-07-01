#task
from django import forms
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'email')
    
 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
                  'country_code', 'phone_number', 'gender' ,'date', 'avatar')


