from rest_framework import serializers

from . import models


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = ('name',)


class LibrarySerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = models.Library
        fields = ('uuid', 'name', 'url', 'publisher', 'dependencies')
