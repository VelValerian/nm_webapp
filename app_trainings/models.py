from django.db import models

class Training(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True)
    bullets = models.JSONField(default=list, blank=True)   # список тезисов
    price = models.PositiveIntegerField()
    duration_min = models.PositiveIntegerField(default=60)
    content = models.TextField(blank=True)                  # развёрнутое описание
    image = models.ImageField(upload_to="trainings/", blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title