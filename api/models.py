from django.db import models


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)


class Article(models.Model):
    category_choices = (
        (1, '咨询'),
        (2, '动态'),
        (3, '分享'),
        (4, '答疑'),
        (5, '其他')
    )
    category = models.IntegerField(verbose_name='分类', choices=category_choices)
    title = models.CharField(verbose_name='主题', max_length=32)
    image = models.CharField(verbose_name='文件路径', max_length=128)
    summary = models.CharField(verbose_name='文章简介', max_length=255)

    author = models.ForeignKey(verbose_name='作者', to='UserInfo')

    comment_count = models.IntegerField(verbose_name='评论数', default=0)
    visit_count = models.IntegerField(verbose_name='浏览数', default=0)
    date = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)


class ArticleDetail(models.Model):
    article = models.OneToOneField(verbose_name='文章表', to='Article')
    content = models.TextField(verbose_name='文章内容')


class Comment(models.Model):
    article = models.ForeignKey(verbose_name='文章表', to='Article')
    content = models.TextField(verbose_name='评论')
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo')

    parent = models.ForeignKey(verbose_name='父评论', to='Comment', null=True, blank=True)
