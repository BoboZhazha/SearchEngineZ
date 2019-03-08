# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from back_spiders.models.es_types import ArticleType


# 讲数据写入到es中
class ElasticsearchPipeline(object):

    def process_item(self, item, spider):
        article = ArticleType()
        article.title = item['title']
        article.detail_url = item['detail_url']
        article.title = item['content']
        article.title = item['grep_time']
        return item


