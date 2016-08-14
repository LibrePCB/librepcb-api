from django.contrib import admin

from . import models


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Library)
class LibraryAdmin(admin.ModelAdmin):
    pass
