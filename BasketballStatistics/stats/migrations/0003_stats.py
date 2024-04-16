# Generated by Django 5.0.4 on 2024-04-16 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=5)),
                ('s_type', models.CharField(max_length=9)),
                ('two_taken', models.IntegerField(default=0)),
                ('two_made', models.IntegerField(default=0)),
                ('three_taken', models.IntegerField(default=0)),
                ('three_made', models.IntegerField(default=0)),
                ('ft_taken', models.IntegerField(default=0)),
                ('ft_made', models.IntegerField(default=0)),
                ('steals', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('turnovers', models.IntegerField(default=0)),
                ('off_rebounds', models.IntegerField(default=0)),
                ('def_rebounds', models.IntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.athlete')),
            ],
        ),
    ]
