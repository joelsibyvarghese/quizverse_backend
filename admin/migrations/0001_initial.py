# Generated by Django 5.0.1 on 2024-03-05 16:51

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0006_verificationtoken"),
    ]

    operations = [
        migrations.CreateModel(
            name="Community",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("level", models.CharField(max_length=100)),
                ("community_type", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "community",
            },
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "department",
            },
        ),
        migrations.CreateModel(
            name="Institution",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("place", models.CharField(max_length=100)),
                (
                    "instituion_type",
                    models.CharField(
                        choices=[("SCHOOL", "school"), ("COLLEGE", "college")],
                        max_length=7,
                    ),
                ),
                ("education_system", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "institution",
            },
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("faculty_id", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
                (
                    "institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin.institution",
                    ),
                ),
            ],
            options={
                "db_table": "faculty",
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("code", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("handling_faculty", models.ManyToManyField(to="admin.faculty")),
            ],
            options={
                "db_table": "course",
            },
        ),
        migrations.CreateModel(
            name="FacultyDepartmentLink",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin.department",
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="admin.faculty"
                    ),
                ),
            ],
            options={
                "db_table": "faculty_department_link",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("roll_number", models.CharField(max_length=100)),
                ("class_or_semester", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin.institution",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
            options={
                "db_table": "student",
            },
        ),
        migrations.CreateModel(
            name="StudentDepartmentLink",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin.department",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="admin.student"
                    ),
                ),
            ],
            options={
                "db_table": "student_department_link",
            },
        ),
    ]
