# Generated by Django 2.2.2 on 2019-07-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0018_delete_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=6),
        ),
        migrations.DeleteModel(
            name='Charge',
        ),
    ]
