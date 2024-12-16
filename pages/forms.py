from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

Position = [
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor'),
]

Gender = [
    ('Male', 'Male'),
    ('Female', 'Female'),
        ('Other', 'Other'),
]
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    Occupation = forms.ChoiceField(choices=Position)
    Gender = forms.ChoiceField(choices=Gender)
    Contact_Number = forms.CharField(max_length=100)
    Address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username','Occupation','Gender','Contact_Number','Address', 'email', 'password1', 'password2', )




 