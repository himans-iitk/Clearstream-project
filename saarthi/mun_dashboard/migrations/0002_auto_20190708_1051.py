# Generated by Django 2.2.3 on 2019-07-08 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mun_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='filer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complaint',
            name='tag',
            field=models.ManyToManyField(related_name='complaints', to='mun_dashboard.Tag'),
        ),
    ]
