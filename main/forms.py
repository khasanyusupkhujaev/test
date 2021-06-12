from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Profile, Comment, Photos

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        for fieldname in ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class EditProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        exclude = ['password']

    def __init__(self, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None

class ProfileImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']

class PhotoFeed(ModelForm):
    class Meta:
        model = Photos
        fields = ['post']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']