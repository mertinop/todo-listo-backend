# Generated by Django 2.1.4 on 2018-12-14 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20180727_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.Estado'),
        ),
    ]
