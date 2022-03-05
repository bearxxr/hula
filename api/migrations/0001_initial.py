# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-03-05 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, '咨询'), (2, '动态'), (3, '分享'), (4, '答疑'), (5, '其他')], verbose_name='分类')),
                ('title', models.CharField(max_length=32, verbose_name='主题')),
                ('image', models.CharField(max_length=128, verbose_name='文件路径')),
                ('summary', models.CharField(max_length=255, verbose_name='文章简介')),
                ('comment_count', models.IntegerField(default=0, verbose_name='评论数')),
                ('visit_count', models.IntegerField(default=0, verbose_name='浏览数')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Article', verbose_name='文章表')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Article', verbose_name='文章表')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Comment', verbose_name='父评论')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='评论者'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserInfo', verbose_name='作者'),
        ),
    ]
