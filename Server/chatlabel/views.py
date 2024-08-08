from rest_framework import viewsets, status
from rest_framework.response import Response
import os
from .models import Filestorage, Textindex, Textlabel
from .serializers import FilestorageSerializer, TextindexSerializer, TextlabelSerializer
from utils import TextnameList
# Create your views here.

class FilestorageView(viewsets.ModelViewSet):
    queryset = Filestorage.objects.all()
    serializer_class = FilestorageSerializer

    def create(self, request, *args, **kwargs):
        serializer = FilestorageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # Get the last file name
            Filename = Filestorage.objects.all().last().file.name
            #Get the column name list from the file
            Index = TextnameList.IndexnameList(Filename)
            #Create the column name list in the Textindex table
            for i in Index:
                Textindex.objects.create(Index=i)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
       
    def delete(self, request, *args, **kwargs):
        '''
        Delete all the data in the Filestorage, Textindex and Textlabel table
        '''
        file = Filestorage.objects.all().last().file.name
        try:
            os.remove(file)
            Filestorage.objects.all().delete()
            Textindex.objects.all().delete()
            Textlabel.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        