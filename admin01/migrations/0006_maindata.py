# Generated by Django 3.2.6 on 2021-12-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0005_over_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maindata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('team_captain', models.CharField(max_length=200)),
                ('team_score', models.CharField(max_length=200)),
                ('team_wicket', models.CharField(max_length=20)),
            ],
        ),
    ]
