from uuid import uuid4

from django.db import models


class AdaptMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return self.message
