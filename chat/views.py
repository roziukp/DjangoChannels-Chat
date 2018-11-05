from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
from django.utils.safestring import mark_safe
from . import forms
from django.views import View
from django.contrib import auth
from . import models
from django.contrib import messages

class Rgistration(View):
    template_name = 'chat/registration.html'
    form_class = forms.UserForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            form.save()
            newuser = auth.authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'], )
            if newuser is not None:
                auth.login(request, newuser)
            return redirect('index')
        else:
            error = "User hasn't been registered!"
            return render(request, self.template_name, {'form': form,
                                                        'error': error})



def index(request):
    room = request.POST.get('room-name')
    if room is not None:
        return redirect('room', room_name=room)
    return render(request, 'chat/index.html', { 'room': room})




def room ( request , room_name ):
    return render ( request , 'chat/room.html' , {
        'room_name_json' : mark_safe ( json . dumps ( room_name ))
    })

