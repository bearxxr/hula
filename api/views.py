from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from api import serializers, models


class ArticleAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            queryset = models.Article.objects.all().order_by('-date')
            pager = PageNumberPagination()
            result = pager.paginate_queryset(queryset, request, self)
            ser = serializers.ArticleListSerializer(instance=result, many=True)
        else:
            article_obj = models.Article.objects.filter(pk=pk).first()
            ser = serializers.PageArticleSerializer(instance=article_obj, many=False)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        ser = serializers.ArticleSerializer(data=request.data)
        ser_content = serializers.ArticleDetailSerializer(data=request.data)
        if ser.is_valid() and ser_content.is_valid():
            article_obj = ser.save(author_id=1)
            ser_content.save(article=article_obj)
        return Response(ser.data)


class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        """ 评论列表 """
        article_id = request.query_params.get('article_id')
        queryset = models.Comment.objects.filter(article_id=article_id)
        ser = serializers.CommentSerializer(instance=queryset, many=True)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        """ 添加评论 """
        ser = serializers.PostCommentSerializer(data=request.data)
        if ser.is_valid():
            ser.save(user_id=1)
            return Response('成功')
        return Response('失败')
