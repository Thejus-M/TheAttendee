from django.shortcuts import render
from .models import student,Attendant

from django.views.generic.list import ListView

class AttendantListView(ListView):
    model = Attendant
    context_object_name = "attendants"
    template_name = "teacher/attendant.html"

