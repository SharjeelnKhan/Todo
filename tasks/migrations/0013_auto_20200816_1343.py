# Generated by Django 3.1 on 2020-08-16 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_auto_20200816_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(default=False, max_length=200),
        ),
    ]