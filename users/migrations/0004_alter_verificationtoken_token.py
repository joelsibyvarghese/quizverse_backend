# Generated by Django 5.0.1 on 2024-05-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_usercommunitylink_accepted_usercommunitylink_role_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="verificationtoken",
            name="token",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
