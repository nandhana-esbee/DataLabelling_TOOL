from django.urls import path, include
from rest_framework import routers

# import viewsets
from .views import FilestorageView,TextlabelView

# create a router object
router = routers.DefaultRouter()

router.register(r'uploadfile',FilestorageView, basename='upload')
router.register(r'label',TextlabelView, basename='label')

urlpatterns = [
	path("", include(router.urls))
]
