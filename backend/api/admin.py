from django.contrib import admin

from .models import Guide, Step


class StepInline(admin.TabularInline):
    model = Step
    extra = 1
    ordering = ["order"]


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "order")
    list_filter = ("category", "featured")
    search_fields = ("title", "summary", "category")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [StepInline]
