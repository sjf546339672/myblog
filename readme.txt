���ӵ�ַ: https://www.bilibili.com/video/BV1i7411e7CY?p=11

���
�����ݿ�����ɵ�ģ�͵���
1. python manage.py inspectdb>movie/models.py

2. def showsql():
...     print(connection.queries[-1]["sql"])

3. ģ��.object.raw("ԭ��SQL���")

4. ��ʾ���ݿ�ͼƬ�ķ���
from django.views.static import serve
if DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}))

5. ����ͼƬ
img_path = os.path.join(os.getcwd(), "media", photo.replace("/", "\\"))
    with open(img_path, 'rb') as fp:
        response = HttpResponse(fp.read())
        response["Content-Type"] = "image/jpg"  # ��ʾ���������е�ý��������Ϣ
        response["Content-Disposition"] = "attachment;filename={}".format(img_name)
        ��HTTP�����У���һ������������inline��Ĭ��ֵ����ʾ�ظ��е���Ϣ�����ҳ���һ���ֻ�������ҳ�����ʽչʾ����
        ������attachment����ζ����Ϣ��Ӧ�ñ����ص����أ����������������һ��������Ϊ���ĶԻ��򣬽�filename��ֵ
        Ԥ��Ϊ���غ���ļ��������������ڵĻ�����
        Content-Disposition: inline
        Content-Disposition: attachment
        Content-Disposition: attachment; filename="filename.jpg"

6.DEBUG=False  ��templates�´���һ��404.html��500.htmlҳ�棬��ôֻҪҳ�����404����ͻ���ʾ��ҳ��

7. �ڲ���һ��������Ϊ��һ���ⲿ�ķ��ؽ����հ�

8. ȫ�������ĵ�ʹ�ã�
(1)��Ӧ���ļ����´���mycontextprocessor.py�ļ����ļ����������д��
(2)Ȼ������Ŀ��settings��TEMPLATES["OPTIONS"]�����"post.mycontextprocessor.getRightInfo"
(3)���ֱ����ҳ����ʹ�øú����ķ������ݼ���

9. haystack six��django3.x�а�װ��������
https://blog.csdn.net/weixin_44485643/article/details/104243048

10.���ı��༭����ʹ��
# ��װ���ļ�
pip install django-ckeditor
# ���õ�����Ӧ��
INSTALLED_APPS = [
    "ckeditor",
    "ckeditor_uploader",  # �ϴ��ļ�ʱ��
]
# ����MEDIAӳ��·��
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
CKEDITOR_UPLOAD_PATH = "upload/"

# ������Ŀ���µ�ӳ��·��
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor', include("ckeditor_uploader.urls")),
]
if DEBUG:
    from django.views.static import serve
    urlpatterns.append(url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT})) # ϵͳ�Զ���ȡ

# �޸�ģ��
from ckeditor_uploader.fields import RichTextUploadingField



ǰ��
1.
<span class="tip"> What's your middle name?</span>
class="tip" ���������Χ��ʡ��

2. �ٶ�һ������ӿڴ���
<div class="bdsharebuttonbox"><a href="#" class="bds_more" data-cmd="more"></a><a href="#" class="bds_qzone" data-cmd="qzone"></a><a href="#" class="bds_tsina" data-cmd="tsina"></a><a href="#" class="bds_tqq" data-cmd="tqq"></a><a href="#" class="bds_renren" data-cmd="renren"></a><a href="#" class="bds_weixin" data-cmd="weixin"></a></div>
<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdPic":"","bdStyle":"0","bdSize":"16"},"share":{},"image":{"viewList":["qzone","tsina","tqq","renren","weixin"],"viewText":"������","viewSize":"16"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","tsina","tqq","renren","weixin"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>


https://www.pythonanywhere.com/user/shijf/  ������Ŀ��վ

















































