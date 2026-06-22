from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("decks", "0017_careeropportunitypage_careeropportunityjob"),
    ]

    operations = [
        migrations.CreateModel(
            name="HiddenSlide",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slide_type", models.CharField(max_length=60)),
                ("object_id", models.PositiveIntegerField()),
                ("removed_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "hidden slide",
                "verbose_name_plural": "hidden slides",
                "ordering": ["-removed_at"],
                "unique_together": {("slide_type", "object_id")},
            },
        ),
    ]
