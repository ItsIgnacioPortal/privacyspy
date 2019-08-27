# Generated by Django 2.2.4 on 2019-08-27 02:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_warning'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginkey',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='warning',
            name='severity',
            field=models.IntegerField(help_text='Possible values: 1 (low), 2 (medium), 3 (high)'),
        ),
    ]
