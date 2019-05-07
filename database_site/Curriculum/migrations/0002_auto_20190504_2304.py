# Generated by Django 2.2 on 2019-05-04 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='grade',
            name='grade_unique',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='Student',
        ),
        migrations.AddField(
            model_name='grade',
            name='Association_ID',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
