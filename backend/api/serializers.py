from rest_framework import serializers

from .models import Guide, Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ["id", "order", "title", "description", "tip"]


class GuideSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Guide
        fields = [
            "id",
            "slug",
            "title",
            "summary",
            "category",
            "emoji",
            "official_url",
            "official_label",
            "featured",
            "order",
            "steps",
        ]
