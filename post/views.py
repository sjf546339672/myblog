import math
import re
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def queryAll(request, num=1):
    num = int(num)
    # 获取所有帖子信息
    postList = Post.objects.all().order_by("-created")
    # 创建分页对象
    paginator = Paginator(postList, 1)
    # 获取当前页数据
    perpageList = paginator.page(num)

    # 生成页码数列表
    # 每页开始页码
    begin = (num - int(math.ceil(10.0/2)))
    if begin < 1:
        begin = 1

    # 每页结束页码
    end = begin + 9
    if end > paginator.num_pages:
        end = paginator.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList = range(begin, end+1)

    return render(request, "index.html", {"postList": perpageList,
                                          "pageList": pageList,
                                          "currentNum": num})


def detail(request, id):
    """阅读全文功能"""
    print(type(id), id)
    # 根据id查询帖子的详情
    postData = Post.objects.get(id=id)
    return render(request, "detail.html", {"postData": postData})


# 根据类别id查询所有帖子
def queryPostByCid(request, id):
    postList = Post.objects.filter(category_id=id)
    return render(request, 'article.html', {'postList': postList})


# 根据发帖时间查询所有帖子
def queryPostByCreated(request, year, month):
    postList = Post.objects.filter(created__year=year, created__month=month)
    return render(request, 'article.html', {'postList': postList})
