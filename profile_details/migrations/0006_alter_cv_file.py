# Generated by Django 4.1.3 on 2023-03-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_details', '0005_cv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='file',
            field=models.FileField(upload_to='CV/'),
        ),
    ]
