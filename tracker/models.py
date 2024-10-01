from django.db import models
from django.core.exceptions import ValidationError


class Game(models.Model):
    title = models.CharField(verbose_name="Game Title", max_length=300)
    platform = models.ForeignKey(
        "Platform", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Game"
        verbose_name_plural = "Games"


class GameVersion(models.Model):
    game = models.ForeignKey(
        "Game",
        on_delete=models.PROTECT,
    )
    version = models.CharField(verbose_name="Version", max_length=300)
    is_archived = models.BooleanField(verbose_name="Archived", default=False)
    is_played = models.BooleanField(verbose_name="Played", default=False)
    is_completed = models.BooleanField(verbose_name="Completed", default=False)
    release_date = models.DateField(verbose_name="Release Date", blank=True, null=True)

    def __str__(self):
        return f"{self.game} ({self.game.platform}) ({self.version})"

    class Meta:
        ordering = ["game"]
        verbose_name = "Game Version"
        verbose_name_plural = "Game Versions"


class Platform(models.Model):
    title = models.CharField(verbose_name="Platform Title", max_length=300)
    release_date = models.DateField(verbose_name="Release Date", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"


class PlatformVersion(models.Model):
    platform = models.ForeignKey("Platform", on_delete=models.PROTECT)
    version = models.CharField(verbose_name="Version", max_length=300)
    is_archived = models.BooleanField(verbose_name="Archived", default=False)
    release_date = models.DateField(verbose_name="Release Date", blank=True, null=True)

    def __str__(self):
        return f"{self.platform.title} ({self.version})"

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
