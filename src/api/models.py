from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Library(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher)
    dependencies = models.ManyToManyField('self', blank=True)

    class Meta:
        verbose_name_plural = 'libraries'

    def __str__(self):
        return '%s by %s' % (self.name, self.publisher.name)
