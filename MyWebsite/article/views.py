from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from .models import *
from read.utils import add_readNum
from comment.models import Comment
from article.forms import ArticleForm


def public_article_list(request,articles):
    context = {}
    paginator = Paginator(articles, 3)
    page_num = request.GET.get('page', 1)
    pages_of_articles = paginator.page(page_num)
    context['articles'] = pages_of_articles
    # 日期归档
    Months = Article.objects.dates('published', 'month', order='DESC')  # 返回时间QuerySet
    date_dict = {}
    for current_month in Months:
        blog_count = Article.objects.filter(published__year=current_month.year,
                                            published__month=current_month.month).count()
        date_dict[current_month] = blog_count
    context['article_dates'] = date_dict
    # 标签归档
    context['article_types'] = Tag.objects.annotate(type_count=Count('article'))

    return context


def article_list(request):
    articles = Article.objects.all()
    context = public_article_list(request,articles)
    return render(request,'article_list.html',context)


def article_with_type(request,tag_id):
    ArticleTag = get_object_or_404(Tag,pk=tag_id)
    articles = Article.objects.filter(tagName=ArticleTag)
    context = public_article_list(request, articles)
    return render(request,'article_with_type.html',context)


def article_with_date(request,year,month):
    articles = Article.objects.filter(published__year=year,published__month=month)
    context = public_article_list(request, articles)
    return render(request,'article_with_date.html',context)


def article_detail(request,article_id):
    context={}
    article = get_object_or_404(Article,id=article_id)
    key = add_readNum(request,article)

    context['article'] = article
    context['previous_article'] = Article.objects.filter(published__lt=article.published).order_by('published').last()
    context['next_article'] = Article.objects.filter(published__gt=article.published).order_by('published').first()

    # article_content_type = ContentType.objects.get_for_model(article)
    # context['comments'] = Comment.objects.filter(content_type=article_content_type, object_id=article.pk,parent=None)
    # context['comment_form'] = CommentForm(initial={'content_type':article_content_type,'object_id':article_id,'reply_id':0})
    response = render(request,'article_detail.html',context)
    response.set_cookie(key,'true')
    return response


def add_article(request):
    context ={}
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,request.FILES)
        if article_form.is_valid():
            title = request.POST.get('title')
            content = request.POST.get('content')
            tagName_list = request.POST.getlist('tagName')
            photo = request.FILES.get('photo')
            print(tagName_list,photo)
            article = Article.objects.create(title=title,content=content, photo=photo,author_id=request.user.uid)
            article.tagName.add(*tagName_list)
            article.save()

            # context["status"] = 'SUCCESS'
            print("ok")
    else:
        article_form = ArticleForm()
    context['article_form'] = article_form
    return render(request,'add_article.html',context)