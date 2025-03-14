# Generated by Django 5.1.6 on 2025-03-09 13:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0004_alter_subscription_subscribed_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscribed_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]
