from django.db import migrations


def seed_guides(apps, schema_editor):
    """Carga las guías iniciales definidas en api/seed_data.py."""
    Guide = apps.get_model("api", "Guide")
    Step = apps.get_model("api", "Step")

    from api.seed_data import GUIDES

    for guide_order, item in enumerate(GUIDES, start=1):
        data = {key: value for key, value in item.items() if key != "steps"}
        guide = Guide.objects.create(order=guide_order, **data)

        for step_order, step in enumerate(item["steps"], start=1):
            Step.objects.create(guide=guide, order=step_order, **step)


def unseed_guides(apps, schema_editor):
    Guide = apps.get_model("api", "Guide")
    Guide.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_guides, unseed_guides),
    ]
