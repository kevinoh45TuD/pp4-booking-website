# Generated by Django 4.2.14 on 2024-07-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Friday')])),
                ('table_one', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('table_two', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('table_three', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('table_four', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('table_five', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('which_movie', models.IntegerField(choices=[(1, 'The Good, The Bad and the Ugly'), (2, 'Planet of the Apes'), (3, 'Enter the Dragon'), (4, 'Escape from Alcatraz'), (5, 'The Godfather'), (6, 'Night of the Living Dead'), (7, 'Monty Python and the Holy Grail')])),
                ('which_year', models.IntegerField()),
                ('which_cuisine', models.CharField()),
            ],
        ),
    ]
