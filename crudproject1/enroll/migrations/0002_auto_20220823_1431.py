# Generated by Django 3.2.7 on 2022-08-23 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stuemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='studentpassword',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stuname',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='stuid',
        ),
    ]
