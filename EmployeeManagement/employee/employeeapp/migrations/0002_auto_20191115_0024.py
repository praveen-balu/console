# Generated by Django 2.2.7 on 2019-11-14 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedetail',
            old_name='lname',
            new_name='contactno',
        ),
        migrations.RenameField(
            model_name='employeedetail',
            old_name='code',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='employeedetail',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='employeedetail',
            name='phone',
        ),
    ]
