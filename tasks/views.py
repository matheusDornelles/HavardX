from audioop import reverse
from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from django.urls import reverse 

tasks = []

class NewTaskform(forms.Form):
    task = forms.CharField(label= "New Task")
    
    
def index (request):
    return render (request, "tasks/index.html",{
        "tasks":tasks
    })

def add(request):
        if request.method == "POST":
            form = NewTaskform(request.POST)
            if form.is_valid():
                task = form.cleaned_data["task"]
                tasks.append(task)
                return HttpResponseRedirect(reverse("tasks:index"))
            else:
                return render (request, "tasks/add.html", {
                    "form" : form
                })
                    

        return render(request, "tasks/add.html", {
            "form": NewTaskform()
        })
                 