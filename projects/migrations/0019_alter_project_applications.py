# Generated by Django 4.1.3 on 2023-02-20 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_remove_project_applications_alter_project_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='applications',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apllications', to='projects.application'),
        ),
    ]
