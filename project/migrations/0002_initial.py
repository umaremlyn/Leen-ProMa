# Generated by Django 4.1.7 on 2023-03-23 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("project", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="user_task",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="task_badge",
            name="badge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="project.badge"
            ),
        ),
        migrations.AddField(
            model_name="task_badge",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="project.project_task"
            ),
        ),
        migrations.AddField(
            model_name="project_team",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="project.project"
            ),
        ),
        migrations.AddField(
            model_name="project_team",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="project_task",
            name="module",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="project.project_module"
            ),
        ),
        migrations.AddField(
            model_name="project_task",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="project.project"
            ),
        ),
        migrations.AddField(
            model_name="project_module",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="project.project"
            ),
        ),
    ]
