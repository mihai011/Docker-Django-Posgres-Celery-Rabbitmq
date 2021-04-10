from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic import ListView

from django.http import JsonResponse, HttpResponse

from .forms import MachineForm, InstanceForm, SparkMasterForm, EnvironmentForm, MLProjectForm, ExperimentForm
from .models import Machine, Instance, SparkMaster, Environment, MLProject, Experiment, Email

from .tasks import mail_send

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.db import IntegrityError, transaction
from django.template.response import TemplateResponse

from django.conf import settings



class MachineView(FormView):

    form_class = MachineForm
    template_name = "form.html"

class InstanceView(FormView):

    form_class = InstanceForm
    template_name = "form.html"

class SparkMasterView(FormView):

    form_class = SparkMasterForm
    template_name = "form.html"

class EnvironmentView(FormView):

    form_class = EnvironmentForm
    template_name = "form.html"

class MLProjectView(FormView):

    form_class = MLProjectForm
    template_name = "form.html"

class ExperimentView(FormView):

    form_class = ExperimentForm
    template_name = "form.html"

class MachineList(ListView):

    model = Machine
    template_name = "list.html"


def email_view(request):


    email = Email(subject="subject", template="template_email.html", froml = "control@gmail.com", to="make@gmail.com")
    email.save()

    transaction.on_commit(lambda: mail_send.delay(email.id))

    return TemplateResponse(request, "template_email.html")