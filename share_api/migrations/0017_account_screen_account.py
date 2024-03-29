# Generated by Django 5.0.2 on 2024-02-09 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_api', '0016_remove_order_customer_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='share_api.service')),
            ],
        ),
        migrations.AddField(
            model_name='screen',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='share_api.account'),
        ),
    ]
