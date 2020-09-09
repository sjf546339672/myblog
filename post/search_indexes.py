# coding: utf-8
#  这个文件名固定必须这样

from haystack import indexes
from post.models import *


# 注意格式(模型类名+Index)
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)  # 固定字段

    # 给title, content设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')
