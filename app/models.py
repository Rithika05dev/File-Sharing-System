from django.db import models
from django.contrib.auth.models import User


class File(models.Model):

    file = models.FileField(upload_to='uploads/')

    filename = models.CharField(max_length=255)

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    version = models.IntegerField(default=1)

    starred = models.BooleanField(default=False)

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.filename


class FileShare(models.Model):

    file = models.ForeignKey(
        File,
        on_delete=models.CASCADE
    )

    shared_with = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    permission = models.CharField(max_length=10)