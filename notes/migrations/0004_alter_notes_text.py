# Generated by Django 3.2.20 on 2023-09-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_notes_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
