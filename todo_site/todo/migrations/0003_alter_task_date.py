# Generated by Django 5.0.1 on 2024-01-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
