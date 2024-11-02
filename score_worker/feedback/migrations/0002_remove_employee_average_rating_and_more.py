# Generated by Django 5.0.6 on 2024-11-02 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='average_rating',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='date_given',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='rating',
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='password123', max_length=128),
        ),
        migrations.AddField(
            model_name='employee',
            name='user_id',
            field=models.CharField(default='394', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='feedback.employee'),
        ),
        migrations.CreateModel(
            name='HardSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hard_skills', to='feedback.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_rating', models.FloatField(default=0.0)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='feedback.employee')),
            ],
        ),
        migrations.CreateModel(
            name='SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('num', models.FloatField(default=0.0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soft_skills', to='feedback.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_text', models.TextField()),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='summary', to='feedback.employee')),
            ],
        ),
    ]
