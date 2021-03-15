from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from django.http import JsonResponse



class BaseView(TemplateView):
    template_name = "base.html"


    