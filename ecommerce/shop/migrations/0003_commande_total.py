# Generated by Django 5.1.7 on 2025-03-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default=500, max_length=200),
            preserve_default=False,
        ),
    ]
