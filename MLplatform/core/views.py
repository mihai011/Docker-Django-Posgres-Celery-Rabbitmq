from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic import ListView

from django.http import JsonResponse

from .forms import *
from .models import *



class MachineView(FormView):

    form_class = MachineForm
    template_name = "base.html"

class InstanceView(FormView):

    form_class = InstanceForm
    template_name = "base.html"

class SparkMasterView(FormView):

    form_class = SparkMasterForm
    template_name = "base.html"

class EnvironmentView(FormView):

    form_class = EnvironmentForm
    template_name = "base.html"

class MLProjectView(FormView):

    form_class = MLProjectForm
    template_name = "base.html"

class ExperimentView(FormView):

    form_class = ExperimentForm
    template_name = "base.html"

class 




    