from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
import os
from .models import Filestorage,Textlabel
from .serializers import FilestorageSerializer,TextlabelSerializer
from utils import Download ,Columns
# Create your views here.

class FilestorageView(viewsets.ModelViewSet):
    queryset = Filestorage.objects.all()
    serializer_class = FilestorageSerializer

    def create(self, request, *args, **kwargs):
        serializer = FilestorageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

    @action(methods=['get'],detail=True) 
    def columnnames(self, request, *args, **kwargs):
        '''
        Get the column names of the uploaded file
        '''
        #get the file id
        id = kwargs.get('pk')
        file = Filestorage.objects.filter(file_id=id).values_list('file', flat=True).first()
        if not file:
            return Response("No file found .Please upload the file.",status=status.HTTP_400_BAD_REQUEST)
        name = Columns.column(file)
        return Response(name) 

    def update(self, request, *args, **kwargs):
        '''
        Update the label name and textname of the uploaded file
        '''
        id = kwargs.get('pk')
        if request.data:
            text = request.data.get('textname')
            label = request.data.get('labelname')
            if text:
                if not label:
                    label = 'label'
                Filestorage.objects.filter(file_id=id).update(labelname=label,textname=text)
                return Response("Data updated successfully",status=status.HTTP_200_OK)
            else:
                return Response("Text name field is required!!!",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("No data found",status=status.HTTP_400_BAD_REQUEST)
      
    def delete(self, request, *args, **kwargs):
        '''
        Delete all the data in the File folder, Filestorage, Textindex and Textlabel table
        '''
        file = Filestorage.objects.all().last().file.name
        try:
            os.remove(file)
            Filestorage.objects.all().delete()
            Textlabel.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class TextlabelView(viewsets.ModelViewSet):
    queryset = Textlabel.objects.all()
    serializer_class = TextlabelSerializer

    def create(self, request, *args, **kwargs):
        serializer = TextlabelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(methods=['get'],detail=True)
    def txtvalue(self, request, *args, **kwargs):
        '''
        Get the text from the uploaded file based on the column name
        '''
        id = kwargs.get('pk')
        indexnum =int(request.query_params.get('index'))
        file = Filestorage.objects.filter(file_id=id).values_list('file', flat=True).first()
        textname = Filestorage.objects.filter(file_id=id).values_list('textname', flat=True).first()

        if not file:
            return Response("No file found .Please upload the file.",status=status.HTTP_400_BAD_REQUEST)
        text  = Columns.Text(file,indexnum ,textname)
        return Response(text)