# Generated by Django 3.2.13 on 2022-04-26 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll_no', models.IntegerField()),
                ('major', models.CharField(max_length=200)),
            ],
        ),
    ]