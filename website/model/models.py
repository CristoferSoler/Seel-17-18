from django.db import models


class BSIArticle(models.Model):
    COMPONENT = 'C'
    THREAT = 'T'
    C_MEASURE = 'CM'
    ARTICLE_TYPE = (
        (COMPONENT, 'Component'),
        (THREAT, 'Threat'),
        (C_MEASURE, 'Countermeasure'),
    )
    id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    article_type = models.CharField(max_length=2, choices=ARTICLE_TYPE) 

    def __str__(self):
        return self.name

    # probably needed - please remove if unused
    def is_component(self):
        return self.article_type in (COMPONENT)

    def is_threat(self):
        return self.article_type in (THREAT)

    def is_countermeasure(self):
        return self.article_type in (C_MEASURE)

    def whatType(self):
        return self.article_type;

