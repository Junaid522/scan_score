from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Document
from django.contrib.auth.forms import UserCreationForm


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )



