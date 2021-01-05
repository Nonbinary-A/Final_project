from django.db import models

# Create your models here.
class Workers(models.Model):

    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    EMAIL = models.CharField(max_length=255)
    PHONE_NUMBER = models.CharField(max_length=255)
    HIRE_DATE = models.DateField()
    JOB_ID = models.CharField(max_length=255)
    SALARY = models.DecimalField(max_digits=10, decimal_places=2)
    COMMISSION_PCT = models.DecimalField(max_digits=3, decimal_places=2)
    MANAGER_ID = models.IntegerField(default=None)
    DEPARTMENT_ID = models.IntegerField(default=None)
    slug = models.SlugField(null=False, unique=True)


    def __str__(self):
        return self.LAST_NAME
