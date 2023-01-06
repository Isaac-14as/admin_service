from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from .models import *

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    ROLE_LIST = (
        ('Оператор', 'Оператор'),
        ('Сотрудник офиса', 'Сотрудник офиса'),
        ('Руководитель', 'Руководитель'),
        ('Администратор', 'Администратор'),
    ) 
    username = forms.CharField(label='Логин', help_text='Логин пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Фамилия и инициалы', help_text='Фамилия и инициалы пользователя должны состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(label='Права доступа', choices=ROLE_LIST)    
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'role', 'password1', 'password2')


class UserChangeCustomFort(UserChangeForm):
    ROLE_LIST = (
        ('Оператор', 'Оператор'),
        ('Сотрудник офиса', 'Сотрудник офиса'),
        ('Руководитель', 'Руководитель'),
        ('Администратор', 'Администратор'),
    ) 
    username = forms.CharField(label='Логин', help_text='Логин пользователя должно состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Фамилия и инициалы', help_text='Фамилия и инициалы пользователя должны состоять максимум из 50 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(label='Права доступа', choices=ROLE_LIST)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'role')



class UserPasswordFort(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('password1', 'password2')


class DateInput(forms.DateInput):
    input_type = 'date'

class MainDataForm(forms.ModelForm):
    year = forms.IntegerField(label='Год')
    cemetery_name = forms.CharField(label='Наименование кладбища', widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.IntegerField(label='Номер')
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'})) 
    age_deceased = forms.IntegerField(label='Возраст умершего')
    date_of_birth = forms.DateField(label='Дата рождения', widget=DateInput)
    date_of_death = forms.DateField(label='Дата смерти', widget=DateInput)
    burial_date = forms.DateField(label='Дата захоронения', widget=DateInput)
    area = forms.CharField(label='Участок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    grave = forms.CharField(label='Могила', widget=forms.TextInput(attrs={'class': 'form-control'}))
    evidence = forms.CharField(label='№ свидетельства о смерти из ЗАГСа', widget=forms.TextInput(attrs={'class': 'form-control'}))
    registry_office = forms.CharField(label='Каким ЗАГСом выдано свидетельство', widget=forms.TextInput(attrs={'class': 'form-control'}))
    responsible_for_burial = forms.CharField(label='Ф.И.О. ответственного за захоронение и его адрес', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    note = forms.CharField(label='Примечание', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    # sys_user = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # sys_data = forms. DateInput(auto_now=False, auto_now_add=True)
    # sys_del = forms.BooleanField(default=False)
    # sys_del_user = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # sys_del_data = forms.DateInput(auto_now=False, auto_now_add=False)

    class Meta:
            model = MainData
            fields = ('year', 'cemetery_name', 'number', 'surname', 'name', 'middle_name', 'age_deceased', 'date_of_birth', 'date_of_death', 'burial_date', 'area', 'grave', 'evidence', 'registry_office', 'responsible_for_burial', 'note')