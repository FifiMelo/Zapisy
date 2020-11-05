# Generated by Django 3.0.6 on 2020-09-28 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Termin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=10)),
                ('teacher_name', models.CharField(max_length=15)),
                ('teacher_surename', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=10)),
                ('hour', models.CharField(max_length=5)),
                ('availble', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uczen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('surename', models.CharField(max_length=15)),
                ('obcy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='zapisy.Termin')),
                ('polski', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='zapisy.Termin')),
            ],
        ),
    ]
