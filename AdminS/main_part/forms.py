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
    year = forms.IntegerField(label='Год', required=False)
    cemetery_name = forms.CharField(label='Наименование кладбища', required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    number = forms.IntegerField(label='Номер', required=False)
    surname = forms.CharField(label='Фамилия', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label='Отчество', required=False, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    age_deceased = forms.IntegerField(label='Возраст умершего', required=False)
    date_of_birth = forms.DateField(label='Дата рождения', required=False, widget=DateInput)
    date_of_death = forms.DateField(label='Дата смерти', required=False, widget=DateInput)
    burial_date = forms.DateField(label='Дата захоронения', required=False, widget=DateInput)
    area = forms.CharField(label='Участок', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    grave = forms.CharField(label='Могила', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    evidence = forms.CharField(label='№ свидетельства о смерти из ЗАГСа', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    registry_office = forms.CharField(label='Каким ЗАГСом выдано свидетельство', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    responsible_for_burial = forms.CharField(label='Ф.И.О. ответственного за захоронение и его адрес', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    note = forms.CharField(label='Примечание', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    # sys_user = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # sys_data = forms. DateInput(auto_now=False, auto_now_add=True)
    # sys_del = forms.BooleanField(default=False)
    # sys_del_user = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # sys_del_data = forms.DateInput(auto_now=False, auto_now_add=False)

    class Meta:
            model = MainData
            fields = ('year', 'cemetery_name', 'number', 'surname', 'name', 'middle_name', 'age_deceased', 'date_of_birth', 'date_of_death', 'burial_date', 'area', 'grave', 'evidence', 'registry_office', 'responsible_for_burial', 'note')
        

class FieldSelection(forms.Form):
    # year = forms.BooleanField(label='Год', required=False, initial=True)
    year = forms.BooleanField(label='Год', required=False)
    cemetery_name = forms.BooleanField(label='Наименование кладбища', required=False)
    number = forms.BooleanField(label='Номер', required=False)
    surname = forms.BooleanField(label='Фамилия', required=False)
    name = forms.BooleanField(label='Имя', required=False)
    middle_name = forms.BooleanField(label='Отчество', required=False) 
    age_deceased = forms.BooleanField(label='Возраст умершего', required=False)
    date_of_birth = forms.BooleanField(label='Дата рождения', required=False)
    date_of_death = forms.BooleanField(label='Дата смерти', required=False)
    burial_date = forms.BooleanField(label='Дата захоронения', required=False)
    area = forms.BooleanField(label='Участок', required=False)
    grave = forms.BooleanField(label='Могила', required=False)
    evidence = forms.BooleanField(label='№ свидетельства о смерти из ЗАГСа', required=False)
    registry_office = forms.BooleanField(label='Каким ЗАГСом выдано свидетельство', required=False)
    responsible_for_burial = forms.BooleanField(label='Ф.И.О. ответственного за захоронение и его адрес', required=False)
    note = forms.BooleanField(label='Примечание', required=False)