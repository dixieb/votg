# Generated by Django 2.2.2 on 2019-06-15 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0002_auto_20190612_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='fname',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='lname',
            new_name='lastName',
        ),
    ]
