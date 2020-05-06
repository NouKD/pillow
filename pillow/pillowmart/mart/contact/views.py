from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from configuration.models import SiteInfo, SocialAccount, OtherInfo, Presentation, Temoignage
from formulaire import ContactForm
from contact.models import NewsLetter
from commerce.models import Categorie, Produit

def index(request):
    #categorie1 = Categorie.objects.get(status=True, nom='quality')
    #categorie2 = Categorie.objects.get(status=True, nom='trending')
    #product_quality = Produit.objects.filter(status=True, categorie=categorie1).order_by('-date_update')[:4]
    #product_trending = Produit.objects.filter(status=True, categorie=categorie2)[:6]
    temoignage = Temoignage.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)
    datas = {
        #'categorie1':categorie,
        #'product_quality_last' : product_quality[0],
        'temoignage' : temoignage,
        #'product_quality': product_quality[1:],
        #'product_trending': product_trending,
        'info_site':info_site,
        'presentation': presentation,
        'social_account': social_account,   
    }
    return render(request, "index.html", datas)

def about(request):
    autresInfo = OtherInfo.objects.filter(status=True)
    temoignage = Temoignage.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'autresInfo': autresInfo,
        'info_site': info_site,
        'presentation': presentation,
        'temoignage': temoignage,
        'social_account': social_account,
    }
    return render(request, "about.html", datas)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()
    autresInfo = OtherInfo.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)
    datas = {
        'autresInfo': autresInfo,
        'contact_form': contact_form,
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "contact.html", datas)

def newsletter(request):
    if request.method == 'Post':
        email = request.POST['newsletter']
        if email:
            news_letter = Newsletter.objects.create(email=email)
            news_letter.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))        

