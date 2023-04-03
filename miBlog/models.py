from django.db import models


class post(models.Model):
    caption_title = models.CharField(max_length=30)
    caption_description = models.CharField(max_length=100)
    heading = models.CharField(max_length=15)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.id} -- {self.heading} -- {self.description}"
# Create your models here.
