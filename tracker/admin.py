from django.contrib import admin
from .models import Game, GameVersion, Platform, PlatformVersion

admin.site.register(Game)
admin.site.register(GameVersion)
admin.site.register(Platform)
admin.site.register(PlatformVersion)
