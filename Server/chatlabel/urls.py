from django.urls import path, include
from rest_framework import routers

# import viewsets
from .views import FilestorageView

# create a router object
router = routers.DefaultRouter()

router.register(r'uploadfile',FilestorageView, basename='upload')

urlpatterns = [
	path("", include(router.urls))
]
