# Generated by Django 3.0.6 on 2020-10-17 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapisy', '0004_remove_uczen_jezyk_obcy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='termin',
            old_name='availble',
            new_name='available',
        ),
        migrations.AddField(
            model_name='uczen',
            name='english_teacher',
            field=models.CharField(default='Karina Zdrzyłowska', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uczen',
            name='foreign_teacher',
            field=models.CharField(default='Monika Lisowska', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uczen',
            name='polish_teacher',
            field=models.CharField(default='Iwona Słowikowska', max_length=15),
            preserve_default=False,
        ),
    ]
