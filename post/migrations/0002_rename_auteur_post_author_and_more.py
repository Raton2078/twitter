# Generated by Django 5.1.6 on 2025-03-05 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auteur',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='contenue',
            new_name='content',
        ),
    ]
