from django.db import models

# Create your models here.

class SocialAccount(models.Model):
    ICONES = [
        ('facebook', 'fab fa-facebook'),
        ('google', 'fab fa-google-plus-g'),
        ('instagrame', 'fab fa-instagram'),
        ('linkedin', 'fab fa-linkedin-in'),
    ]
    nom = models.CharField(max_length = 255)
    liens = models.URLField()
    icone = models.CharField(choices=ICONES, max_length=20)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="social account"
        verbose_name_plural = "socials accounts"

    def __str__(self):
        return self.nom  


class SiteInfo(models.Model):
    map_url = models.TextField()
    email = models.EmailField()
    logo = models.ImageField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Site Info"
        verbose_name_plural = "Site Infos"

    def __str__(self):
        return self.email

class Presentation(models.Model):
    nom = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Produit')
    video = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Presentation"
        verbose_name_plural = "Presentations"

    def __str__(self):
        return self.nom 


    
class Temoignage(models.Model):
    photo = models.ImageField()
    nom = models.CharField(max_length = 255)
    prenom = models.CharField(max_length = 255)
    messages = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Temoignage"
        verbose_name_plural = "Temoignage"

    def __str__(self):
        return self.nom       

