# Generated by Django 4.0.3 on 2022-04-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.IntegerField(primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=60)),
                ('studentClass', models.CharField(max_length=20)),
            ],
        ),
    ]
