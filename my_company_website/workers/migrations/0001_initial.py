# Generated by Django 3.1.4 on 2021-01-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRST_NAME', models.CharField(max_length=255)),
                ('LAST_NAME', models.CharField(max_length=255)),
                ('EMAIL', models.CharField(max_length=255)),
                ('PHONE_NUMBER', models.CharField(max_length=255)),
                ('JOB_ID', models.CharField(max_length=255)),
                ('SALARY', models.DecimalField(decimal_places=2, max_digits=10)),
                ('COMMISSION_PCT', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]