from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=254, label="ФИО", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}))
    username = forms.CharField(max_length=254, label="Логин", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(max_length=254, min_length=6, label="Пароль", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '******'}))
    phone = forms.CharField(max_length=254, label="Номер телефона", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (ххх)-ххх-хх-хх'}))
    email = forms.EmailField(max_length=254, label="Почта", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = 'full_name', 'username', 'password', 'phone', 'email'