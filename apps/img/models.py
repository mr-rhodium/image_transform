from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_uuid = models.TextField(unique=True, help_text="ID in S3 bucked")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Created at")

    def __str__(self):
        return f"{self.user}: {self.image_uuid}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Image"
        verbose_name_plural = "Images"
