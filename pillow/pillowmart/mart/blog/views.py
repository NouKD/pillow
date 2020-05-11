from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from configuration.models import SiteInfo, SocialAccount, Presentation, UserAccount, OtherInfo
from blog.models import CategorieArticle, Tag, Article, Commentaire


def blog(request, filtre=None, id=None):
    if filtre == 'categories':
        articles = Article.objects.filter(status=True, categorie=id)
    elif filtre == 'tag':
        articles = Article.objects.filter(status=True, tag=id)
    else:
        articles = Article.objects.filter(status=True)

    _paginator = Paginator(articles, 5)
    page = request.GET.get('page')

    try:
        articles_page = _paginator.page(page)
    except PageNotAnInteger: # Si le numero de page n'est pas un entier
        articles_page = _paginator.page(1)
    except EmptyPage: # Si la page est vide
        articles_page = _paginator.page(_paginator.num_pages)

    tags = Tag.objects.filter(status=True)
    categories = CategorieArticle.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]

    datas = {
        'articles': articles_page,
        'tags': tags,
        'categories': categories,
        'recent_articles': articles.order_by('-date_update')[:4],
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "pages/blog.html", datas)



def single_blog(request, id):
    _article = get_object_or_404(Article, id=id, status=True)
    if request.method == 'POST':
        if request.user.is_authenticated:
            commentaire = request.POST['comment']
            if commentaire:
                user = UserAccount.objects.get(status=True, user=request.user)
                if user:
                    poster_commentaire = Commentaire.objects.create(
                        article=_article,
                        user=user,
                        commentaire=commentaire
                        )
                    poster_commentaire.save()
        else:
            return redirect('login')

    
    autresInfo = OtherInfo.objects.filter(status=True)[0]
    tags = Tag.objects.filter(status=True)
    articles = Article.objects.filter(status=True)
    comment = Commentaire.objects.filter(status=True, article=_article)
    categories = CategorieArticle.objects.filter(status=True)
    info_site = SiteInfo.objects.filter(status=True)[0]
    social_account = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[0]
    datas = {
        'autresInfo': autresInfo,
        'commentaires': comment,
        'article': _article,
        'tags': tags,
        'categories': categories,
        'recent_articles': articles.order_by('-date_update')[:4],
        'info_site': info_site,
        'presentation': presentation,
        'social_account': social_account,
    }
    return render(request, "pages/single-blog.html", datas)
