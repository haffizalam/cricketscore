# Generated by Django 3.2.6 on 2022-01-04 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0011_batsman_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='opponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin01.team')),
            ],
        ),
    ]
