# Generated by Django 5.1 on 2025-06-20 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='note_tag',
            name='tag',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='note.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=32, unique=True),
        ),
    ]
