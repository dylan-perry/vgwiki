from django.contrib import admin
from import_export import resources, fields, widgets
from .models import Game, GameVersion, Platform, PlatformVersion
from import_export.admin import ImportExportModelAdmin

class GameResource(resources.ModelResource):

    class Meta:
        model = Game
        fields = ('id', 'name', 'url', 'summary', 'first_release_date', 'platforms')

    def get_import_fields(self):
        fields = super().get_import_fields()
        for field in fields:
            if field.column_name == 'summary':
                field.attribute = 'description'
            if field.column_name == 'first_release_date':
                field.attribute = 'release_date'
        return fields

    platform = fields.Field(
        column_name='platforms',
        attribute='platform',
        widget=widgets.ForeignKeyWidget(Platform, 'id')
    )

    def after_import_row(self, row, row_result, **kwargs):
        
        platform_ids = row['platforms'][1:-1].split(',')
        name = row['name']

        for platform_id in platform_ids:
            platform = Platform.objects.get(pk=int(platform_id.strip()))
            Game.objects.create(name=name, platform=platform)

        return row_result

class PlatformResource(resources.ModelResource):

    class Meta:
        model = Platform
        fields = ('id', 'name', 'url', 'generation')


class GameAdmin(ImportExportModelAdmin):
    resource_classes = [GameResource]

class GameVersionAdmin(ImportExportModelAdmin):
    list_display = ('game_name', 'version', 'release_date', 'is_archived', 'played_status')

    def game_name(self, obj):
        return obj.game.name
    
    # resource_classes = [GameVersionResource]

class PlatformAdmin(ImportExportModelAdmin):
    list_display = ('name', 'release_date', 'url', 'generation')

    resource_classes = [PlatformResource]


admin.site.register(Game, GameAdmin)
admin.site.register(GameVersion, GameVersionAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(PlatformVersion)
