import django.forms as forms


class UserRegister(forms.Form):
    username = forms.CharField(label='Введите логин', min_length=3, max_length=30)
    password = forms.CharField(label='Введите пароль', min_length=8, max_length=30)
    repeat_password = forms.CharField(label='Повторите пароль', min_length=8, max_length=30)
    age = forms.IntegerField(label='Введите свой возраст', min_value=18, max_value=99, error_messages={
        'min_value': 'Вы должны быть старше 18', 'max_value': 'Вы не должны быть старше 100'
    })