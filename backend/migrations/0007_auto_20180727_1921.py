# Generated by Django 2.0.4 on 2018-07-27 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20180727_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend.Estado'),
        ),
    ]
