from django.db import models
from django.core.exceptions import ValidationError


class Game(models.Model):
    title = models.CharField(verbose_name="Game Title", max_length=300)
    platform = models.ForeignKey(
        "Platform", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Game"
        verbose_name_plural = "Games"


class GameVersion(models.Model):
    game = models.ForeignKey(
        "Game",
        on_delete=models.PROTECT,
    )
    version = models.CharField(verbose_name="Version", blank=True, max_length=300)
    is_archived = models.BooleanField(verbose_name="Archived")
    is_played = models.BooleanField(verbose_name="Played")
    is_completed = models.BooleanField(verbose_name="Completed")
    release_date = models.DateField(verbose_name="Release Date", blank=True)

    class Meta:
        ordering = ["game"]
        verbose_name = "Game Version"
        verbose_name_plural = "Game Versions"


class Platform(models.Model):
    name = models.CharField(verbose_name="Platform Name", max_length=300)
    release_date = models.DateField(verbose_name="Release Date")

    class Meta:
        ordering = ["name"]
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"


class PlatformVersion(models.Model):
    platform = models.ForeignKey("Platform", on_delete=models.PROTECT)
    version = models.CharField(verbose_name="Version", blank=True, max_length=300)
    is_archived = models.BooleanField(verbose_name="Archived")
    release_date = models.DateField(verbose_name="Release Date", blank=True)

    class Meta:
        ordering = ["platform"]
        verbose_name = "Platform Version"
        verbose_name_plural = "Platform Versions"

    # TODO: Not sure if any of the below are necessary yet
    # def clean(self):
    #     super().clean() # Call the parent class's clean method

    # def save(self, *args, **kwargs):
    #     # Ensuring clean method validation
    #     self.clean()
    #     super().save(*args, *kwargs)

    # def __str__(self):
    #     # Setting title field as identifier for admin panel
    #     return self.title
