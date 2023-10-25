```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['cv', 'cover_letter']

    def clean_cv(self):
        cv = self.cleaned_data.get('cv', False)
        if cv:
            if cv.size > 2*1024*1024:
                raise forms.ValidationError("CV file too large ( > 2mb )")
            return cv
        else:
            raise forms.ValidationError("Couldn't read uploaded CV")

    def clean_cover_letter(self):
        cover_letter = self.cleaned_data.get('cover_letter', False)
        if cover_letter:
            if cover_letter.size > 2*1024*1024:
                raise forms.ValidationError("Cover letter file too large ( > 2mb )")
            return cover_letter
        else:
            raise forms.ValidationError("Couldn't read uploaded cover letter")
```