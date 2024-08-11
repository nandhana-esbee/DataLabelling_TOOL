from django.db import models

# Create your models here.

class Filestorage(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='files/')
    textname= models.CharField(max_length=100, null=True) 
    labelname = models.CharField(max_length=100, default='label')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    

class Textlabel(models.Model):
    text_id = models.AutoField(primary_key=True)
    text = models.TextField()
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.text