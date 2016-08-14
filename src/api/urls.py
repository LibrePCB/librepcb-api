from django.conf.urls import url, include

from rest_framework import routers

from . import views

# Create router
router = routers.DefaultRouter()

# Register resources
router.register(r'libraries', views.LibraryViewSet)

# Create URLs
urlpatterns = [
    url(r'^', include(router.urls)),
]
