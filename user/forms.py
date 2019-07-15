from django import forms
from django.contrib.auth import authenticate
from user.models import User


class LoginForm(forms.Form):
    email = forms.CharField(label='Електронна пошта')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if (not email) or (not user):
            raise forms.ValidationError('Невірний пароль або email.')
        return password


class UserCreationForm(forms.ModelForm):
    """
    реєстрація клієнта
    """
    class Meta:
        model = User
        exclude = ('is_staff', 'created', 'modified', 'last_login')

    field_order = ['email', 'first_name', 'last_name', 'date_birth', 'post', 'image', ]

    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, required=False, label='Повторіть пароль')
    date_birth = forms.DateField(label='Дата народження', widget=forms.TextInput(attrs={'id': 'datetimepicker1'}))

    def clean_email(self):
        data = self.cleaned_data['email']
        if len(data) < 6:
            raise forms.ValidationError(_(u'Електронна пошта має мати мінімум 6 символів'))
        if self.instance:
            c = User.objects.filter(email=data).exclude(pk=self.instance.pk).count()
        else:
            c = User.objects.filter(email=data).count()
        if c:
            raise forms.ValidationError('Ця електронна пошта вже використовується!')
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) < 6:
            raise forms.ValidationError('Пароль мінімум 6 символів!')
        return data

    def clean_password2(self):
        data = self.cleaned_data.get('password', None)
        data2 = self.cleaned_data['password2']
        if data != data2:
            raise forms.ValidationError('Паролі не збігаються!')
        return data2


class UserEditForm(forms.ModelForm):
    """
    редагування клієнта
    """
    class Meta:
        model = User
        exclude = ('created', 'modified', 'last_login', 'password')
