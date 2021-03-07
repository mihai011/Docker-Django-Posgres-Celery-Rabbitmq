from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm, GenerateRandomNumberForm, GenerateRandomNameForm
from .tasks import create_random_user_accounts, create_random_number, create_random_name
from .models import Name
from .models import Number


class BaseView(TemplateView):
    template_name = "base.html"

class UsersListView(ListView):
    template_name = 'users_list.html'
    model = User

class NamesListView(ListView):
    template_name = 'names_list.html'
    model = Name

class NumbersListView(ListView):
    template_name = 'numbers_list.html'
    model = Number


class GenerateRandomUserView(FormView):
    template_name = 'generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')

class GenerateRandomNameView(FormView):
    template_name = 'generate_random_names.html'
    form_class = GenerateRandomNameForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_name.delay(total)
        messages.success(self.request, 'We are generating your random names! Wait a moment and refresh this page.')
        return redirect('names_list')

class GenerateRandomNumberView(FormView):
    template_name = 'generate_random_users.html'
    form_class = GenerateRandomNumberForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        t = create_random_number.delay(total)
        messages.success(self.request, 'We are generating your random numbers! Wait a moment and refresh this page.')
        return redirect('numbers_list')