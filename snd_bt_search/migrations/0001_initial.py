# Generated by Django 4.1.10 on 2023-08-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SndBroadcast",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("broadcast_year", models.CharField(max_length=4)),
                ("broadcast_month", models.CharField(max_length=2)),
                ("broadcast_date", models.CharField(max_length=8)),
                ("broadcast_content", models.CharField(max_length=400)),
                ("assistant_1", models.CharField(max_length=200)),
                ("assistant_2", models.CharField(max_length=200)),
                ("guests", models.CharField(max_length=100)),
                ("remarks", models.CharField(max_length=400)),
            ],
            options={
                "db_table": "snd_broadcast",
            },
        ),
    ]
