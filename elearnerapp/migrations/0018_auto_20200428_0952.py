# Generated by Django 2.2.5 on 2020-04-28 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elearnerapp', '0017_auto_20200428_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_text', models.CharField(max_length=500)),
                ('option_a', models.CharField(max_length=500)),
                ('option_b', models.CharField(max_length=500)),
                ('option_c', models.CharField(max_length=500)),
                ('option_d', models.CharField(max_length=500)),
                ('correct', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=5)),
                ('is_correct', models.BooleanField(default=False)),
                ('ques', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elearnerapp.Question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elearnerapp.Questionnaire'),
        ),
    ]
