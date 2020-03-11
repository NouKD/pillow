from django.db import models

# Create your models here.


class Categorie(models.Model):
    nom = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Categorie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nom




class Produit(models.Model):
    nom = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images/Produit')
    description = models.TextField()
    prix= models.FloatField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='article_produit')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.nom