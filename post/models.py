from django.db import models

# Create your models here.


class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name="类别名称")

    class Meta:
        db_table = "t_category"
        verbose_name_plural = u"类别"

    def __str__(self):
        return u"Category: {}".format(self.cname)


class Tag(models.Model):
    tname = models.CharField(max_length=30, unique=True, verbose_name="标签名称")

    class Meta:
        db_table = "t_tag"
        verbose_name_plural = u"标签"

    def __str__(self):
        return u"Tag: {}".format(self.tname)


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="标题")
    desc = models.CharField(max_length=100, verbose_name="描述")
    content = models.TextField(verbose_name="内容")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    categpry = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="类别")
    tag = models.ManyToManyField(Tag, verbose_name="标签")

    class Meta:
        db_table = "t_post"
        verbose_name_plural = "帖子"

    def __str__(self):
        return u"Post: {}".format(self.title)

