from main.models import Author,Book
from django import forms


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname','email')