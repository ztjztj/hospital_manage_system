# Generated by Django 2.1.2 on 2019-07-15 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='fk_doctor_user',
        ),
        migrations.RemoveField(
            model_name='patienttwo',
            name='patient_one_fk',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='PatientTwo',
        ),
    ]
