# Generated by Django 5.0.4 on 2024-08-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_cellphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photography',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
