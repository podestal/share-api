# Generated by Django 5.0.1 on 2024-01-20 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_api', '0009_alter_screen_due_date_alter_screen_subscribed_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='share_api.service')),
            ],
        ),
    ]
