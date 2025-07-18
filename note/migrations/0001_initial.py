# Generated by Django 5.1 on 2025-06-20 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('content', models.CharField(blank=True, max_length=256, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['modification_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Note_Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.note')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.tag')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(through='note.Note_Tag', to='note.tag'),
        ),
    ]
