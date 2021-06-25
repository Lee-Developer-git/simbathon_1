from allauth.account.forms import LoginForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs = {
            'type': 'text',
            'placeholder': '아이디',
        })

class SignupForm(forms.Form):
    class Meta:
        model = User

    gender = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': '성별'}))
    kakao = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '카카오 오픈 톡'}))
    club = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': '동아리명'}))

    def signup(self, request, user):
        userProfile = Profile()
        userProfile.user = user
        userProfile.gender = self.cleaned_data['gender']
        userProfile.kakao = self.cleaned_data['kakao']
        userProfile.club = self.cleaned_data['club']
        userProfile.save()
        user.save()
        return user