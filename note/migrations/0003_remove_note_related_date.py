# Generated by Django 5.1.4 on 2024-12-25 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_note_content_note_created_at_note_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='related_date',
        ),
    ]
