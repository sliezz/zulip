# Generated by Django 4.2.8 on 2023-12-25 00:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0056_remoterealm_realm_locally_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="remoterealm",
            name="last_request_datetime",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="remotezulipserver",
            name="last_request_datetime",
            field=models.DateTimeField(null=True),
        ),
    ]