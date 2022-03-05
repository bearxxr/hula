from django.conf.urls import include, url

from api import views

urlpatterns = [
    # 文章接口
    url(r'^article/$', views.ArticleAPIView.as_view(), name='article'),
    url(r'^article/(?P<pk>\d+)/$', views.ArticleAPIView.as_view(), name='article'),

    # 评论接口
    url(r'^comment/$', views.CommentView.as_view(), name='comment'),
]
