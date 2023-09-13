from django import forms
from .models import Notes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class PostForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'keywords', 'header_image','text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Title Here"}),
            'keywords': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Keywords" }),
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder':"Notes Here"})
        }



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name =forms.CharField(max_length=100)
    last_name =forms.CharField(max_length=100)
    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')