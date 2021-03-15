from django.test import TestCase
from .models import Environment
# Create your tests here.

class TestEnvironment(TestCase):

    def setUp(self):
        pass

    def test_control(self):

        env = Environment()
        

