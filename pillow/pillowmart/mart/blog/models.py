from django.db import models
from configuration.models import UserAccount
# Create your models here.

class CategorieArticle(models.Model):
    nom = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images/CategorieArticle')
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="categoriearticle"
        verbose_name_plural = "categoriearticles"

    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.nom 

class Article(models.Model):
    titre= models.CharField(max_length = 255)
    description = models.TextField()
    contenue = models.TextField()
    image = models.ImageField(upload_to='images/Article')
    tag = models.ManyToManyField(Tag,related_name="Tag_Article")
    categorie = models.ForeignKey(CategorieArticle, on_delete=models.CASCADE, related_name='Article')
    auteur = models.ForeignKey(UserAccount, related_name='auteur_article', on_delete=models.CASCADE, null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.titre         

class Commentaire(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='commentaire_article')
    user = models.ForeignKey(UserAccount, related_name='comment_user', on_delete=models.CASCADE, null=True)
    #nom = models.CharField(max_length = 255)
    #prenom = models.CharField(max_length = 255)
    commentaire = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="commentaire"
        verbose_name_plural = "commentaires"

    def __str__(self):
        return self.user         