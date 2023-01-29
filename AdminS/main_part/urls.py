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
    path('record_list/', record_list, name='record_list'),
    path('utilities_list/', utilities_list, name='utilities_list'),

    # для карты 
    # path('utilities_list/', utilities_list, name='utilities_list'),
    path('record_del/<int:record_id>/', record_del, name='record_del'),
    path('record_edit/<int:record_id>/', record_edit, name='record_edit'),

    path('search/', search, name='search'),
    path('search_result/', search_result, name='search_result'),
    path('basket/', basket, name='basket'),
    path('record_edit_basket/<int:record_id>/', record_edit_basket, name='record_edit_basket'),
    path('record_del_basket/<int:record_id>/', record_del_basket, name='record_del_basket'),

    path('settings/', settings, name='settings'),
]   
