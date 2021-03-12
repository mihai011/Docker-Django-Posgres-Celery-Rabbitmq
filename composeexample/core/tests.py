from django.test import TestCase
from .tasks import mail_send
# Create your tests here.

class TestMail(TestCase):

    def test_mail_simple(self):

        # executes on ques, will send mail
        v = mail_send.delay()
        print(v)
        # executes locally, will not send mail
        v = mail_send()
        print(v)
        

