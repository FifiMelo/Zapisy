# Generated by Django 3.0.6 on 2020-10-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapisy', '0005_auto_20201017_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uczen',
            name='english_teacher',
            field=models.CharField(max_length=31),
        ),
        migrations.AlterField(
            model_name='uczen',
            name='foreign_teacher',
            field=models.CharField(max_length=31),
        ),
        migrations.AlterField(
            model_name='uczen',
            name='polish_teacher',
            field=models.CharField(max_length=31),
        ),
    ]