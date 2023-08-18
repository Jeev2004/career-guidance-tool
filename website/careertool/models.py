from django.db import models
from django.conf import settings

class s1(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default='Default Author')
    Circuit_Design = models.IntegerField(default=0, null=True)
class s2(models.Model):
    Control_Systems = models.IntegerField(default=0, null=True)
class s3(models.Model):
    Power_Electronics = models.IntegerField(default=0, null=True)
class s4(models.Model):
    Analog_Communication = models.IntegerField(default=0, null=True)
class s5(models.Model):
    R_F = models.IntegerField(default=0, null=True)
class s6(models.Model):
    C_P_P = models.IntegerField(default=0, null=True)
class s7(models.Model):
    Electrical_System = models.IntegerField(default=0, null=True)
class s8(models.Model):
    C_A_D = models.IntegerField(default=0, null=True)
class s9(models.Model):
    P_C_B = models.IntegerField(default=0, null=True)
class s10(models.Model):
    Lab_View = models.IntegerField(default=0, null=True)
