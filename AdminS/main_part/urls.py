from django.urls import path

from .views import *
 
urlpatterns = [
    path('index/', index, name='index'), 
    path('', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    path('create_user/', create_user, name='create_user'),
    path('all_users/', all_users, name='all_users'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('edit_user_password/<int:user_id>/', edit_user_password, name='edit_user_password'),
    path('create_entry/', create_entry, name='create_entry'),

]
