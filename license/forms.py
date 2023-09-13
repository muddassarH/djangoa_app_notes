from django import forms
from lisc.models import License

class DataEntryForm(forms.ModelForm):
    class Meta:
        model = License
        fields = '__all__'



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']