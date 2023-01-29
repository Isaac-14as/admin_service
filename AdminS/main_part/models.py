from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_LIST = (
        ('Оператор', 'Оператор'),
        ('Сотрудник офиса', 'Сотрудник офиса'),
        ('Руководитель', 'Руководитель'),
        ('Администратор', 'Администратор'),
    ) 
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30, verbose_name='Права доступа', choices=ROLE_LIST)
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
 
    def __str__(self):
        return self.username

# , validators=[MinValueValidator(0), MaxValueValidator(150)]
class MainData(models.Model):
    year = models.IntegerField(verbose_name='Год', blank=True, null=True)
    cemetery_name = models.CharField(verbose_name='Наименование кладбища',max_length=512, blank=True, null=True)
    number = models.IntegerField(verbose_name='Номер', blank=True, null=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=40, blank=True, null=True)
    name = models.CharField(verbose_name='Имя', max_length=40, blank=True, null=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=40, blank=True, null=True) 
    age_deceased = models.IntegerField(verbose_name='Возраст умершего', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', auto_now=False, auto_now_add=False, blank=True, null=True)
    date_of_death = models.DateField(verbose_name='Дата смерти', auto_now=False, auto_now_add=False, blank=True, null=True)
    burial_date = models.DateField(verbose_name='Дата захоронения', auto_now=False, auto_now_add=False, blank=True, null=True)
    area = models.CharField(verbose_name='Участок', max_length=50, blank=True, null=True)
    grave = models.CharField(verbose_name='Могила', max_length=50, blank=True, null=True)
    evidence = models.CharField(verbose_name='№ свидетельства о смерти из ЗАГСа', max_length=50, blank=True, null=True)
    registry_office = models.CharField(verbose_name='Каким ЗАГСом выдано свидетельство', max_length=10, blank=True, null=True)
    responsible_for_burial = models.TextField(verbose_name='Ф.И.О. ответственного за захоронение и его адрес', blank=True, null=True)
    note = models.TextField(verbose_name='Примечание', blank=True, null=True)
    user_create = models.CharField(verbose_name='Создатель записи', max_length=50)
    data_create = models.DateTimeField(verbose_name='Дата создания записи', auto_now=False, auto_now_add=True)
    del_status = models.BooleanField(default=False, null=True)
    del_user = models.CharField(max_length=50, blank=True, null=True)
    del_data = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

