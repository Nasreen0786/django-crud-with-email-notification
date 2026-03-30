from django.db import models

# makemigration-create changes and store in the file
# migrate-apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

class Service(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name