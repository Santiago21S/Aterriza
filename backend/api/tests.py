from rest_framework import status
from rest_framework.test import APITestCase

from .models import Guide


class HealthTests(APITestCase):
    def test_health(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["status"], "ok")


class GuideApiTests(APITestCase):
    def test_list_guides(self):
        response = self.client.get("/api/guides/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        guides = response.json()
        self.assertGreaterEqual(len(guides), 10)

        slugs = {guide["slug"] for guide in guides}
        self.assertIn("primeros-7-dias", slugs)
        self.assertIn("empadronamiento", slugs)
        self.assertIn("medico", slugs)

    def test_guide_detail_includes_ordered_steps(self):
        response = self.client.get("/api/guides/primeros-7-dias/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        guide = response.json()
        self.assertTrue(guide["steps"])
        self.assertEqual(guide["steps"][0]["title"], "Empadrónate en tu municipio")

        orders = [step["order"] for step in guide["steps"]]
        self.assertEqual(orders, sorted(orders))

    def test_guides_are_read_only(self):
        initial_count = Guide.objects.count()

        response = self.client.post(
            "/api/guides/",
            {"title": "Guía inventada", "summary": "No debería crearse"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Guide.objects.count(), initial_count)
