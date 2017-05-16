from django import urls
from django.shortcuts import render, redirect
from section import views


def to_main(request):
    return redirect('/sections/')
