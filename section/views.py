from django.shortcuts import render, redirect
from django.http import JsonResponse
from section import forms
from section.models import Section, Student


def login(request):
    if request.method == 'POST':
        form = forms.login_form(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            students = Student.objects.filter(sid=student_id)
            if len(students) > 0 and password == students[0].password:
                request.session['sid'] = student_id
            else:
                return render(request, "section/login.html", {'form': form})
            return redirect('/sections/')
        else:
            return render(request, "section/login.html", {'form': form})
    form = forms.login_form()
    return render(request, "section/login.html", {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = forms.sign_up_form(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password == password2:
                new_student = Student()
                new_student.name = name
                new_student.sid = student_id
                new_student.password = password
                new_student.save()
                return redirect('/sections/login')

    form = forms.sign_up_form()
    return render(request, "section/signup.html", {'form': form})


def sections(request):
    sid = request.session.get('sid')
    if sid is None:
        return redirect('/sections/login')
    else:
        student = Student.objects.get(sid=sid)
        sections = student.section_set.all()
        sections_list = []
        names_set = set()
        for section in sections:
            sections_list.append((section.date, section.course.name))
            names_set.add(section.course.name)
        return render(request, 'section/sections.html', {'sections': sections_list, 'names': names_set})


def all_sections(request):
    sections = Section.objects.all()
    sections_list = []
    names_set = set()
    for section in sections:
        sections_list.append((section.date, section.course.name, section.id))
        names_set.add(section.course.name)
    return render(request, 'section/all_sections.html', {'sections': sections_list, 'names': names_set})


def register(request):
    if request.method == 'GET':
        student_sid = request.session.get('sid')
        if student_sid is None:
            student_sid = request.GET.get('sid')
            if student_sid is None:
                return JsonResponse({'success': False, 'message': 'wrong parameters: student sid is missing'})

        section_id = request.GET.get('id')
        if section_id is None:
            return JsonResponse({'success': False, 'message': 'wrong parameters: section id is missing'})

        student = Student.objects.get(sid=student_sid)
        section = Section.objects.get(pk=section_id)

        for s in student.section_set.all():
            if s.course.id == section.course.id:
                return JsonResponse({'success': True})

        if section.students.count() < 25:
            section.students.add(student)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'section is full'})
    return JsonResponse({'success': False, 'message': 'wrong method'})


def log_out(request):
    del request.session['sid']
    return JsonResponse({'success': True})
