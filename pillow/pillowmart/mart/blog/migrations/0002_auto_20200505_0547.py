# Generated by Django 2.2.10 on 2020-05-05 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_otherinfo_useraccount'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='commentaire',
            name='prenom',
        ),
        migrations.AddField(
            model_name='article',
            name='auteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auteur_article', to='configuration.UserAccount'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to='configuration.UserAccount'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire_article', to='blog.Article'),
        ),
    ]