from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
import datetime 

from django.contrib.auth import login, logout
from .forms import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


def index(request):
    template = "main_part/index.html"
    response = render(request, template)
    response.set_cookie('year', True)
    response.set_cookie('cemetery_name', True)
    response.set_cookie('number', True)
    response.set_cookie('surname', True)
    response.set_cookie('name', True)
    response.set_cookie('middle_name', True)
    response.set_cookie('age_deceased', True)
    response.set_cookie('date_of_birth', True)
    response.set_cookie('date_of_death', True)
    response.set_cookie('burial_date', True)
    response.set_cookie('area', True)
    response.set_cookie('grave', True)
    response.set_cookie('evidence', True)
    response.set_cookie('registry_office', True)
    response.set_cookie('responsible_for_burial', True)
    response.set_cookie('note', True)
    return response

def user_login(request):
    template = "main_part/login.html"
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

def user_logout(request):
    logout(request)
    return redirect('user_login')


def create_user(request):
    template = "main_part/create_user.html"
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировали нового пользователя')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

def all_users(request):
    template = "main_part/all_users.html"
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, template, context)

def delete_user(request, user_id):
    template = "main_part/delete_user.html"
    user_del = User.objects.get(id=user_id)
    context = {
        'user_del': user_del,
    }
    if request.method == 'POST':
        user_del.delete()
        return redirect(all_users)
    return render(request, template, context)


def edit_user(request, user_id):
    template = "main_part/edit_user.html"
    user_edit = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserChangeCustomFort(request.POST, instance=user_edit)
        if form.is_valid():
            form.save()
            return redirect(all_users)
    else:
        form = UserChangeCustomFort(instance=user_edit)

    context = {
        'form': form,
        'user_edit': user_edit,
        'user_id': user_id,
    }

    return render(request, template, context)

def edit_user_password(request, user_id):
    template = "main_part/edit_user_password.html"
    user_edit = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserPasswordFort(request.POST, instance=user_edit)
        if form.is_valid():
            form.save()
            return redirect(all_users)
    else:
        form = UserPasswordFort(instance=user_edit)

    context = {
        'form': form,
        'user_edit': user_edit,
    }

    return render(request, template, context)

def create_entry(request):
    template = "main_part/create_entry.html"
    if request.method == 'POST':
        form = MainDataForm(request.POST)
        if form.is_valid():
            record = form.save()
            record.user_create = str(request.user.username)
            record.save()
    else:
        form = MainDataForm()
    context = {
        'form': form,
    }
    return render(request, template, context)


# тут изменить кол-во записей и добавить пагинацию
def record_list(request):
    template = "main_part/record_list.html"
    if request.user.role == 'Оператор':
        record = MainData.objects.filter(user_create=request.user.username).filter(del_status=False).order_by('-data_create')
        m = []
        for i in record:
            if i.data_create.strftime("%Y-%m-%d") == datetime.datetime.today().strftime("%Y-%m-%d"):
                m.append(i)
        if len(m) == 0:
            record = record[:10]
    else:
        record = MainData.objects.filter(user_create=request.user.username).order_by('-data_create')[:10]
    context = {
        'record': record,
    }
    return render(request, template, context) 


def utilities_list(request):
    template = "main_part/utilities_list.html"
    return render(request, template) 



# дописать вот эти две функции
def search(request):
    template = "main_part/search.html"
    if request.method == 'POST':
        form = MainDataForm(request.POST)
        if form.is_valid():
            year_1 = str(form.cleaned_data.get('year'))
            cemetery_name_1 = str(form.cleaned_data.get('cemetery_name'))
            number_1 = str(form.cleaned_data.get('number'))
            surname_1 = str(form.cleaned_data.get('surname'))
            name_1 = str(form.cleaned_data.get('name'))
            middle_name_1 = str(form.cleaned_data.get('middle_name'))
            age_deceased_1 = str(form.cleaned_data.get('age_deceased'))
            date_of_birth_1 = str(form.cleaned_data.get('date_of_birth'))
            date_of_death_1 = str(form.cleaned_data.get('date_of_death'))
            burial_date_1 = str(form.cleaned_data.get('burial_date'))
            area_1 = str(form.cleaned_data.get('area'))
            grave_1 = str(form.cleaned_data.get('grave'))
            evidence_1 = str(form.cleaned_data.get('evidence'))
            registry_office_1 = str(form.cleaned_data.get('registry_office'))
            responsible_for_burial_1 = str(form.cleaned_data.get('responsible_for_burial'))
            note_1 = str(form.cleaned_data.get('note'))

            # return redirect(search_result, str(form.cleaned_data.get('year')), str(form.cleaned_data.get('cemetery_name')))
            # return redirect(f'/search_result/{year_1}/{cemetery_name_1}/')
            return redirect(f'/search_result?year={year_1}&cemetery_name={cemetery_name_1}&number={number_1}&surname={surname_1}&name={name_1}&middle_name={middle_name_1}&age_deceased={age_deceased_1}&date_of_birth={date_of_birth_1}&date_of_death={date_of_death_1}&burial_date={burial_date_1}&area={area_1}&grave={grave_1}&evidence={evidence_1}&registry_office={registry_office_1}&responsible_for_burial={responsible_for_burial_1}&note={note_1}')
            # return redirect(f'/search_result/{year_1}/')
    else:
        form = MainDataForm()

    context = {
        'form': form,
    }

    return render(request, template, context)


def search_result(request):
    d_1 = {
        'year': request.GET.get('year'),
        'cemetery_name': request.GET.get('cemetery_name'),
        'number': request.GET.get('number'),
        'surname': request.GET.get('surname'),
        'name': request.GET.get('name'),
        'middle_name': request.GET.get('middle_name'),
        'age_deceased': request.GET.get('age_deceased'),
        'date_of_birth': request.GET.get('date_of_birth'),
        'date_of_death': request.GET.get('date_of_death'),
        'burial_date': request.GET.get('burial_date'),
        'area': request.GET.get('area'),
        'grave': request.GET.get('grave'),
        'evidence': request.GET.get('evidence'),
        'registry_office': request.GET.get('registry_office'),
        'responsible_for_burial': request.GET.get('responsible_for_burial'),
        'note': request.GET.get('note'),
    }
    d_2 = {
        'year': False,
        'cemetery_name': False,
        'number': False,
        'surname': False,
        'name': False,
        'middle_name': False,
        'age_deceased': False,
        'date_of_birth': False,
        'date_of_death': False,
        'burial_date': False,
        'area': False,
        'grave': False,
        'evidence': False,
        'registry_office': False,
        'responsible_for_burial': False,
        'note': False,
    }
    template = "main_part/search_result.html"
    record = MainData.objects.filter(del_status=False).order_by('-data_create')
    m = []
    for i in record:
        d_3 = {
            'year': i.year,
            'cemetery_name': i.cemetery_name,
            'number': i.number,
            'surname': i.surname,
            'name': i.name,
            'middle_name': i.middle_name,
            'age_deceased': i.age_deceased,
            'date_of_birth': i.date_of_birth,
            'date_of_death': i.date_of_death,
            'burial_date': i.burial_date,
            'area': i.area,
            'grave': i.grave,
            'evidence': i.evidence,
            'registry_office': i.registry_office,
            'responsible_for_burial': i.responsible_for_burial,
            'note': i.note,
        }
        for key, value in d_1.items():
            if (d_1[key] != 'None' and len(d_1[key]) != 0):
                if d_1[key] in str(d_3[key]):
                    d_2[key] = True
            else:
                d_2[key] = True
        flag = True
        for key, value in d_2.items():
            if d_2[key] == False:
                flag = False
            d_2[key] = False
        print(flag)
                
        if flag:
            m.append(i)

    record = m
    context = {
        'record': record,
    }
    return render(request, template, context) 





# окончательное удаление

# def record_del_finally(request, record_id):
#     template = "main_part/record_del_finally.html"
#     record = MainData.objects.get(id=record_id)
#     context = {
#         'record': record,
#     }
#     if request.method == 'POST':
#         record.delete()
#         return redirect(record_list)
#     return render(request, template, context)


def record_del(request, record_id):
    template = "main_part/record_del.html"
    record = MainData.objects.get(id=record_id)
    context = {
        'record': record,
    }
    if request.method == 'POST':
        record.del_status = True
        record.save()
        return redirect(record_list)
    return render(request, template, context)



def record_edit(request, record_id):
    template = "main_part/record_edit.html"
    record = MainData.objects.get(id=record_id)
    if request.method == 'POST':
        form = MainDataForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect(record_list)
    else:
        form = MainDataForm(instance=record)
    date_of_birth = str(record.date_of_birth)
    date_of_death = str(record.date_of_death)
    burial_date = str(record.burial_date)
    context = {
        'form': form,
        'record': record,
        'date_of_birth': date_of_birth,
        'date_of_death': date_of_death,
        'burial_date': burial_date,
    }
    return render(request, template, context)


def basket(request):
    template = "main_part/basket.html"
    record = MainData.objects.filter(del_status=True)
    context = {
        'record': record,
    }
    return render(request, template, context)


def record_edit_basket(request, record_id):
    template = "main_part/record_edit.html"
    record = MainData.objects.get(id=record_id)
    if request.method == 'POST':
        form = MainDataForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect(basket)
    else:
        form = MainDataForm(instance=record)
    context = {
        'form': form,
        'record': record,
    }
    return render(request, template, context)

def record_del_basket(request, record_id):
    template = "main_part/record_del.html"
    record = MainData.objects.get(id=record_id)
    context = {
        'record': record,
    }
    if request.method == 'POST':
        record.delete()
        return redirect(basket)
    return render(request, template, context)

def settings(request):
    template = "main_part/settings.html"
    context = {
        'form': FieldSelection()
    }
    response = render(request, template, context)

    if request.method == 'POST':
        form = FieldSelection(request.POST)
        if form.is_valid():
            year = form['year'].value()
            cemetery_name = form['cemetery_name'].value()
            number = form['number'].value() 
            surname = form['surname'].value()
            name = form['name'].value()
            middle_name = form['middle_name'].value() 
            age_deceased = form['age_deceased'].value() 
            date_of_birth = form['date_of_birth'].value()
            date_of_death = form['date_of_death'].value() 
            burial_date = form['burial_date'].value() 
            area = form['area'].value() 
            grave = form['grave'].value() 
            evidence = form['evidence'].value() 
            registry_office = form['registry_office'].value() 
            responsible_for_burial = form['responsible_for_burial'].value() 
            note = form['note'].value()
            response.set_cookie('year', year)
            response.set_cookie('cemetery_name', cemetery_name)
            response.set_cookie('number', number)
            response.set_cookie('surname', surname)
            response.set_cookie('name', name)
            response.set_cookie('middle_name', middle_name)
            response.set_cookie('age_deceased', age_deceased)
            response.set_cookie('date_of_birth', date_of_birth)
            response.set_cookie('date_of_death', date_of_death)
            response.set_cookie('burial_date', burial_date)
            response.set_cookie('area', area)
            response.set_cookie('grave', grave)
            response.set_cookie('evidence', evidence)
            response.set_cookie('registry_office', registry_office)
            response.set_cookie('responsible_for_burial', responsible_for_burial)
            response.set_cookie('note', note)
    return response
