# Generated by Django 3.2.6 on 2021-12-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0009_show_over'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target_run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TR', models.CharField(max_length=100)),
            ],
        ),
    ]
