from django.db import models


class LandingEntry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
