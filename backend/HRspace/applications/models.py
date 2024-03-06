from django.db import models


class Сandidate(models.Model):
    """Соискатель."""
    cv = models.FileField(upload_to="uploads/")
