from django.db import models

# Create your models here.

class Filestorage(models.Model):
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
class Textindex(models.Model):
    Index = models.CharField(max_length=100)

class Textlabel(models.Model):
    textname= models.ForeignKey(Textindex, on_delete=models.CASCADE)
    text = models.TextField()
    labelname = models.CharField(max_length=100)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.labelname