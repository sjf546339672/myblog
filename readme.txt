链接地址: https://www.bilibili.com/video/BV1i7411e7CY?p=11

后端
将数据库表生成到模型当中
1. python manage.py inspectdb>movie/models.py

2. def showsql():
...     print(connection.queries[-1]["sql"])

3. 模型.object.raw("原生SQL语句")

4. 显示数据库图片的方法
from django.views.static import serve
if DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}))

5. 下载图片
img_path = os.path.join(os.getcwd(), "media", photo.replace("/", "\\"))
    with open(img_path, 'rb') as fp:
        response = HttpResponse(fp.read())
        response["Content-Type"] = "image/jpg"  # 表示具体请求中的媒体类型信息
        response["Content-Disposition"] = "attachment;filename={}".format(img_name)
        在HTTP场景中，第一个参数或者是inline（默认值，表示回复中的消息体会以页面的一部分或者整个页面的形式展示），
        或者是attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，将filename的值
        预填为下载后的文件名，假如它存在的话）。
        Content-Disposition: inline
        Content-Disposition: attachment
        Content-Disposition: attachment; filename="filename.jpg"

6.DEBUG=False  在templates下创建一个404.html、500.html页面，那么只要页面出现404报错就会显示该页面

7. 内部的一个函数作为它一个外部的返回叫做闭包

8. 全局上下文的使用，
(1)在应用文件夹下创建mycontextprocessor.py文件（文件名可以随便写）
(2)然后在项目的settings中TEMPLATES["OPTIONS"]中添加"post.mycontextprocessor.getRightInfo"
(3)最后直接在页面上使用该函数的返回数据即可

9. haystack six在django3.x中安装问题问题
https://blog.csdn.net/weixin_44485643/article/details/104243048

10.富文本编辑器的使用
# 安装库文件
pip install django-ckeditor
# 配置第三方应用
INSTALLED_APPS = [
    "ckeditor",
    "ckeditor_uploader",  # 上传文件时用
]
# 配置MEDIA映射路径
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
CKEDITOR_UPLOAD_PATH = "upload/"

# 配置项目包下的映射路径
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor', include("ckeditor_uploader.urls")),
]
if DEBUG:
    from django.views.static import serve
    urlpatterns.append(url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT})) # 系统自动读取

# 修改模型
from ckeditor_uploader.fields import RichTextUploadingField



前端
1.
<span class="tip"> What's your middle name?</span>
class="tip" 超出这个范围就省略

2. 百度一键分享接口代码
<div class="bdsharebuttonbox"><a href="#" class="bds_more" data-cmd="more"></a><a href="#" class="bds_qzone" data-cmd="qzone"></a><a href="#" class="bds_tsina" data-cmd="tsina"></a><a href="#" class="bds_tqq" data-cmd="tqq"></a><a href="#" class="bds_renren" data-cmd="renren"></a><a href="#" class="bds_weixin" data-cmd="weixin"></a></div>
<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdPic":"","bdStyle":"0","bdSize":"16"},"share":{},"image":{"viewList":["qzone","tsina","tqq","renren","weixin"],"viewText":"分享到：","viewSize":"16"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","tsina","tqq","renren","weixin"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>


https://www.pythonanywhere.com/user/shijf/  部署项目网站

















































