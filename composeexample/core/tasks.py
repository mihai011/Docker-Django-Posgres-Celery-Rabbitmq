import string
import random

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task
from .models import Name, Number

from celery.decorators import task

from django.core.mail import send_mail


@task(queue="heavy")
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    print('{} random users created with success!'.format(total))
    return '{} random users created with success!'.format(total)

@task(queue="medium")
def create_random_name(total):
    for i in range(total):
        firstname = get_random_string(10)
        familyname = get_random_string(20)
        Name.objects.create(first_name=firstname, family_name=familyname)
    print('{} random names created with success!'.format(total))
    return '{} random names created with success!'.format(total)

@task(queue="easy")
def create_random_number(total):
    for i in range(total):
        number = random.randrange(0,100)
        Number.objects.create(number=number)
    print('{} random numbers created with success!'.format(total))
    return '{} random numbers created with success!'.format(total)

@task(queue="heavy")
def mail_send():

    v = send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
    )

    return v

