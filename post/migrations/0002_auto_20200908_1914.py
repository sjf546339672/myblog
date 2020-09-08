# Generated by Django 3.0.5 on 2020-09-08 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='category',
            name='cname',
            field=models.CharField(max_length=30, unique=True, verbose_name='类别名称'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categpry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Category', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='描述'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='post.Tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tname',
            field=models.CharField(max_length=30, unique=True, verbose_name='标签名称'),
        ),
    ]
