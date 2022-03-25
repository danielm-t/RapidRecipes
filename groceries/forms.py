from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def clean(self):
        clean_data = super(UserForm, self).clean()
        password = clean_data.get('password')

        if password is not None:
            if len(password) < 6:
                raise forms.ValidationError('Password is too short')
