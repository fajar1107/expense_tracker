# forms.py
from django.forms import ModelForm
from .models import TrackerIncomeExpense
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class IncomeExpenseForm(ModelForm):
    class Meta:
        model = TrackerIncomeExpense
        exclude = ['user']  # Exclude the 'user' field from the form

class StatementDateForm(forms.Form):
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']