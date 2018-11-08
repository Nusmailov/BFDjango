from main.models import User, Restaurant
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'surname', 'email')

