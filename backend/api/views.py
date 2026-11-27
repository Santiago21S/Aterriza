from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Guide
from .serializers import GuideSerializer


@api_view(["GET"])
def health(request):
    """Endpoint sencillo para comprobar que Django está vivo."""
    return Response({"status": "ok", "service": "django"})


class GuideViewSet(viewsets.ReadOnlyModelViewSet):
    """Guías de solo lectura. El contenido se edita desde el admin de Django."""

    queryset = Guide.objects.prefetch_related("steps").all()
    serializer_class = GuideSerializer
    lookup_field = "slug"
