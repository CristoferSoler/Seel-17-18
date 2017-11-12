from .models import BSIArticle


class BSIArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BSIArticle
        fields = ('id', 'location', 'article_type')
        # fields = '__all__'