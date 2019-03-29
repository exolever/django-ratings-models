from django.contrib import admin

from . import models


class InteractionAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'rating',
        'created', 'edited',
    )


admin.site.register(models.Interaction, InteractionAdmin)
admin.site.register(models.OverallRating)
admin.site.register(models.Rating)
admin.site.register(models.SkipRating)
