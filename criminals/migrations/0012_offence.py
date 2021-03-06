# Generated by Django 2.2.2 on 2019-07-16 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0011_delete_offence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offence', models.CharField(max_length=255)),
                ('enactment', models.CharField(max_length=1000)),
                ('fixed_penalty', models.CharField(max_length=10)),
                ('penalty_points', models.CharField(max_length=5)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criminals.Person')),
            ],
        ),
    ]
