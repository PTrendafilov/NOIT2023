# Generated by Django 4.1.3 on 2023-01-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
