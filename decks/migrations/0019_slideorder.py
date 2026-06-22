from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("decks", "0018_hiddenslide"),
    ]

    operations = [
        migrations.CreateModel(
            name="SlideOrder",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slide_type", models.CharField(max_length=60)),
                ("object_id", models.PositiveIntegerField()),
                ("position", models.PositiveIntegerField(default=1)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "slide order",
                "verbose_name_plural": "slide orders",
                "ordering": ["position", "id"],
                "unique_together": {("slide_type", "object_id")},
            },
        ),
    ]
