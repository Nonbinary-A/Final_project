from rest_framework import serializers
from .models import Workers
class WorkersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Workers
       fields = ['id', 'FIRST_NAME', 'LAST_NAME', 'EMAIL',\
                 'PHONE_NUMBER', 'HIRE_DATE', 'JOB_ID',\
                 'SALARY', 'COMMISSION_PCT', 'MANAGER_ID',\
                 'DEPARTMENT_ID']