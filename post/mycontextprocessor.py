# coding: utf-8
from django.db.models import Count

from post.models import Post


def getRightInfo(request):
    # 1. 获取分类信息
    right_category = Post.objects.values("category__cname", "category").annotate(c=Count("*")).order_by("-c")

    # 2.近期文章
    right_recent_post = Post.objects.all().order_by("-created")[:3]

    # 获取日期归档信息
    from django.db import connection
    sql = "select created, count('*') from t_post GROUP BY DATE_FORMAT(created,'%Y-%m') ORDER BY created desc"
    cur = connection.cursor()
    cur.execute(sql)
    right_fill_post = cur.fetchall()
    return {"right_category": right_category, "right_recent_post": right_recent_post, "right_fill_post": right_fill_post}
