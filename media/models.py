from django.db import models
import cloudinary.models


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField(help_text="Upload photo to Cloudinary and paste URL here")

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField(help_text="Upload video to ImageKit.io and paste URL here")

    def __str__(self):
        return self.title



