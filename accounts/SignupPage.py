from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    age = forms.PositiveIntegerField()
    userID = forms.CharField(max_length=100)
    role = forms.ChoiceField(choices=[('doctor', 'Doctor'), ('patient', 'Patient')])

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'age', 'userID', 'role')
