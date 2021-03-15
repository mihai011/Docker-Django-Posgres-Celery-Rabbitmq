from django.db import models

# Create your models here.

class Machine(models.Model):

    name = models.CharField(blank=True, max_length=15)
    API_URL = models.CharField(blank=True, max_length=512)

class Instance(Machine):

    ip = models.CharField(blank=True, max_length=15)
    host = models.CharField(blank=True, max_length=100)
    RSA_KEY = models.CharField(blank=True, max_length=1024)
    ssh_user = models.CharField(blank=True, max_length=64)

class SparkMaster(Machine):

    SPARK_URL = models.CharField(blank=True, max_length=126)

class Environment(models.Model):

    machine = models.ForeignKey(Machine, on_delete=models.RESTRICT)
    requirements = models.FileField()
    py_version = models.FloatField()

class MLProject(models.Model):

    file = models.FileField()

class Experiment(models.Model):

    project = models.ForeignKey(MLProject, on_delete=models.RESTRICT)
    env = models.ForeignKey(Environment, on_delete=models.RESTRICT)