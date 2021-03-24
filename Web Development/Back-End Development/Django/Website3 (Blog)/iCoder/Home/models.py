from django.db import models


# Create your models here.
# Database is like a Excel Workbook
# Models are like Sheets in Excel
class Contact(models.Model):
    SerialNumber = models.AutoField(primary_key=True)  # primary key is like a unique identifier
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email
