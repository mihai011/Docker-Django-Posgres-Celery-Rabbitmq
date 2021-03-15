>>> from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import *


class MachineForm(ModelForm):

    class Meta:

        model = Machine
        fields = ['name', 'API_URL']
        

class InstanceForm(ModelForm):

    class Meta:

        model = Instance
        fields = ['ip_address', 'host', 'RSA_KEY', 'ssh_user']

class SparkMasterForm(ModelForm):

    class Meta:

        model = SparkMaster
        fields = ['SPARK_URL']

class EnvironmentForm(ModelForm):

    class Meta:

        model = Environment
        fields = ['machine', 'requirements', 'py_version']

class MLProjectForm(ModelForm):

    class Meta:

        model = MLProject
        fields = ['file']

class ExperimentForm(ModelForm):

    class Meta:

        model = Experiment
        fields = ['project', 'env']






