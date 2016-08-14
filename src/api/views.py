from rest_framework import viewsets

from . import models, serializers


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = models.Library.objects.all()
    serializer_class = serializers.LibrarySerializer
