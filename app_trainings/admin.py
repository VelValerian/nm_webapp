from django.contrib import admin
from .models import Training

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "duration_min")
    search_fields = ("title", "subtitle", "slug")
    prepopulated_fields = {"slug": ("title",)}