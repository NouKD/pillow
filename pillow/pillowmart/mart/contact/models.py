from django.db import models

# Create your models here.

class Contact(models.Model):
    message = models.TextField()
    nom = models.CharField(max_length = 255)
    mail = models.EmailField()
    sujet = models.CharField(max_length = 255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="contact"
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.nom 

class NewsLetter(models.Model):
    mail = models.EmailField() 
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="newsLetter"
        verbose_name_plural = "newsletters"

    def __str__(self):
        return str(self.mail)   

