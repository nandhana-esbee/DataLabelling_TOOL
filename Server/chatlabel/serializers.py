from rest_framework import serializers
from .models import Filestorage, Textlabel

class FilestorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filestorage
        fields = '__all__'

class TextlabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textlabel
        fields = '__all__'