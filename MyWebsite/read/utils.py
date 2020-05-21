import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum, ReadDetail
from article.models import Article

def add_readNum(request,obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_read' % (ct.model,obj.pk)
    if not request.COOKIES.get(key):
        read_num,created = ReadNum.objects.get_or_create(content_type=ct,object_id=obj.pk)
        read_num.read_num += 1
        read_num.save()

        readD_detail_num, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk,read_date=timezone.now().date())
        readD_detail_num.read_num += 1
        readD_detail_num.save()
    return key


def seven_days_readNum(content_type):
    today = timezone.now().date()
    readNum_list = []
    dates_list=[]
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates_list.append(date.strftime('%m/%d'))
        read_detail  = ReadDetail.objects.filter(content_type = content_type,read_date=date)
        result = read_detail.aggregate(read_sum=Sum('read_num'))
        readNum_list.append(result['read_sum'] or 0)
    return dates_list,readNum_list


def hot_article(days_ago):
    today = timezone.now().date()
    seven_date = today - datetime.timedelta(days=days_ago)
    hot_articles = Article.objects.filter(
        read_details__read_date__gt=seven_date,read_details__read_date__lt=today).\
        values('id','title','published').annotate(articles=Sum('read_details__read_num')).\
        order_by('-read_details__read_num')
    return hot_articles