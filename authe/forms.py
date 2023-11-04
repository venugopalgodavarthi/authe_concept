from django import forms
from authe.models import user_model
from django.contrib.auth.hashers import make_password


class user_form(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user_model
        fields = ['username', 'first_name', 'last_name', 'email',
                  'phone', 'gender', 'dob', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        print(self.cleaned_data['password'])
        user.password = make_password(self.cleaned_data['password'])
        print(user.password)
        if commit == True:
            user.save()
        return user


class login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
