from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from . import models
from . import forms

@login_required
def welcome(request):
    contexto = {"productos": models.Flan.objects.filter(is_private=True)}
    return render(request, "welcome.html", contexto)


def about(request):
    contexto = {}
    return render(request, "about.html", contexto)


def index(request):
    contexto = {"productos": models.Flan.objects.filter(is_private=False)}
    return render(request, "index.html", contexto)


def contacto(request):
    formulario = forms.ContactFormForm
    if request.method == "POST":
        form = formulario(request.POST)
        if form.is_valid():
            models.ContactForm.objects.create(**form.cleaned_data)
            return redirect("exito")
    elif request.method == "GET":
        form = formulario()
    contexto = {"form": form}
    return render(request, "contactus.html", contexto)


def exito(request):
    contexto = {}
    return render(request, "success.html", contexto)

def receta(request):
    contexto = {}
    return render(request, "receta.html", contexto)