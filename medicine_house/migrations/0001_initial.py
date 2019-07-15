# Generated by Django 2.0 on 2019-07-14 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=20)),
                ('medicine_number', models.IntegerField()),
                ('medicine_outer_price', models.FloatField()),
                ('medicine_enter_price', models.FloatField()),
                ('medicine_message', models.CharField(max_length=200)),
                ('fk_medicine_type_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_register.Department')),
            ],
        ),
    ]
