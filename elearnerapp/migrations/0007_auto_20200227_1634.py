# Generated by Django 2.1.2 on 2020-02-27 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearnerapp', '0006_auto_20200227_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='ques',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
