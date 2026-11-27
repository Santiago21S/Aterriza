from django.db import models


class Guide(models.Model):
    """Guía práctica sobre un trámite o tarea del día a día."""

    slug = models.SlugField("identificador", unique=True)
    title = models.CharField("título", max_length=120)
    summary = models.TextField("resumen")
    category = models.CharField("categoría", max_length=60)
    emoji = models.CharField("icono", max_length=8, default="📘")
    official_url = models.URLField("enlace oficial", blank=True)
    official_label = models.CharField(
        "texto del enlace oficial", max_length=90, blank=True
    )
    featured = models.BooleanField("destacada", default=False)
    order = models.PositiveIntegerField("orden", default=0)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "guía"
        verbose_name_plural = "guías"

    def __str__(self) -> str:
        return self.title


class Step(models.Model):
    """Un paso concreto dentro de una guía."""

    guide = models.ForeignKey(
        Guide, related_name="steps", on_delete=models.CASCADE, verbose_name="guía"
    )
    order = models.PositiveIntegerField("orden", default=0)
    title = models.CharField("título", max_length=140)
    description = models.TextField("descripción")
    tip = models.CharField("consejo", max_length=260, blank=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "paso"
        verbose_name_plural = "pasos"

    def __str__(self) -> str:
        return f"{self.guide.title} · {self.title}"
