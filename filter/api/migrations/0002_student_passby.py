# Generated by Django 4.1.7 on 2024-01-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passby',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]
