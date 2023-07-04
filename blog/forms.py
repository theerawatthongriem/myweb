from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class RegisterForm(UserCreationForm):
    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'ชื่อผู้ใช้'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'ชื่อ'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'นามสกุล'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'อีเมล'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'รหัสผ่าน'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'ยืนยันรหัสผ่าน'
        })

    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','password1','password2']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['avatar']

