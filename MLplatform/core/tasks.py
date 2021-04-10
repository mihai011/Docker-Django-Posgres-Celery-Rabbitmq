import string
import random

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task
from .models import  Email

from celery.decorators import task

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.template import Context

from django.conf import settings



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
def mail_send(id):

    email = Email.objects.get(id=id)

    subject = email.subject
    to = [email.to]
    from_email = email.froml

    ctx = {
        'user': 'buddy',
        'purchase': 'Books',
        'image_src': "http://{}/static/admin/img/download.jpg".format(settings.STATIC_HOST)
    }

    message = get_template(email.template).render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
