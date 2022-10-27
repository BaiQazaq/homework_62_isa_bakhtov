# Generated by Django 4.1.2 on 2022-10-27 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker_app', '0004_projectuser_project_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuser',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_user', to='tracker_app.project', verbose_name="User's project"),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_project', to=settings.AUTH_USER_MODEL, verbose_name="User's project"),
        ),
    ]
