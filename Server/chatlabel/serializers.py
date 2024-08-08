from rest_framework import serializers
from .models import Filestorage, Textindex, Textlabel

class FilestorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filestorage
        fields = '__all__'

class TextindexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textindex
        fields = '__all__'

class TextlabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textlabel
        fields = '__all__'