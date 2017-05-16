from django.shortcuts import render, redirect
from django.http import JsonResponse
from section import forms, models
import database_handler as handler


def login(request):
    form = forms.login_form()
    if request.method == 'POST':
        form = forms.login_form(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            row = handler.query_user(id)
            if row is not None and password in row:
                request.session['sid'] = id
            else:
                render(request, "section/login.html", {'form': form})
            return redirect('/sections/')
        else:
            render(request, "section/login.html", {'form': form})
    return render(request, "section/login.html", {'form': form})


def sign_up(request):
    form = forms.sign_up_form()
    if request.method == 'POST':
        form = forms.sign_up_form(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password == password2:
                handler.insert_user(name, password, sid=id)
                return redirect('/sections/login')

    return render(request, "section/signup.html", {'form': form})


def sections(request):
    sid = request.session.get('sid')
    if sid is None:
        return redirect('/sections/login')
    else:
        student_id = handler.query_user(sid)[0]
        (sections_list, names_set) = handler.query_student_sections(student_id=student_id)
        return render(request, 'section/courses.html', {'sections': sections_list, 'names': names_set})


def all_sections(request):
    (sections_list, names_set) = handler.query_sections()
    return render(request, 'section/courses.html', {'sections': sections_list, 'names': names_set})


def register(request):
    if request.method == 'GET':
        student_sid = request.session.get('sid')
        if student_sid is None:
            student_sid = request.GET.get('sid', '')
            if student_sid is None:
                return JsonResponse({'success': False, 'message': 'wrong parameters: student sid is missing'})

        section_id = request.GET.get('id', '')
        if section_id is None:
            return JsonResponse({'success': False, 'message': 'wrong parameters: section id is missing'})

        student_id = handler.query_user(student_sid)[0]
        if handler.register(section_id=section_id, student_id=student_id):
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'section is full'})
    return JsonResponse({'success': False, 'message': 'wrong method'})


def log_out(request):
    del request.session['sid']
    return JsonResponse({'success': True})


def test(request):
    student_id = request.session.get('sid')
    if request.method == 'GET':
        section_id = request.GET.get('id', '')
        handler.register(section_id=section_id, student_id=student_id)
    return render(request, "section/test.html", {'s': request.session.get('sid')})

# TODO: if not signed in check if id in the param
