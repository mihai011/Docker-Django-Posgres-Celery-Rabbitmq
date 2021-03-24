from django.test import TestCase, TransactionTestCase 
from .models import Environment, Email
from .tasks import mail_send
from django.db import transaction
from django.core import mail


# Create your tests here.

class TestEnvironment(TestCase):

    def setUp(self):
        pass

    def test_control(self):

        env = Environment()

class TestEmail(TestCase):

    def setUp(self):

        self.email = Email(subject="Test", message="message", froml = "control@gmail.com", to="make@gmail.com")
        self.email.save()

    def test_email_function(self):

        mail_send(self.email.id)
        self.assertEqual(len(mail.outbox), 1)

    
    def test_email_apply(self):

        res = mail_send.apply(kwargs={"id":self.email.id})
        self.assertEqual(len(mail.outbox), 1)

    def tearDown(self):

        self.email.delete()