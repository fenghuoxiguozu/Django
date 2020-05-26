from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from read.utils import seven_days_readNum,hot_article
from article.models import Article



def index(request):
    context={}
    content_type = ContentType.objects.get_for_model(Article)
    dates_list,read_nums = seven_days_readNum(content_type=content_type)

    three_hot_articles = cache.get('three_hot_articles')
    seven_hot_articles = cache.get('seven_hot_articles')
    thirty_hot_articles = cache.get('thirty_hot_articles')
    if three_hot_articles is None:
        three_hot_articles = hot_article(3)
        seven_hot_articles = hot_article(7)
        thirty_hot_articles = hot_article(30)
        cache.set('three_hot_articles',three_hot_articles,3600)
        cache.set('seven_hot_articles', seven_hot_articles,3600)
        cache.set('thirty_hot_articles', seven_hot_articles,3600)

    context['read_nums'] = read_nums
    context['dates_list'] = dates_list
    context['three_hot_articles'] = three_hot_articles
    context['seven_hot_articles'] = seven_hot_articles
    context['thirty_hot_articles'] = thirty_hot_articles
    return render(request,'chart.html',context)


