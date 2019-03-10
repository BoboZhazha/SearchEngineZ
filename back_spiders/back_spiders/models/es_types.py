#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-08 10:50
# @Author  : zhangshanbo
# @File    : es_types.py
# @Remark:


from elasticsearch_dsl import DocType, Date, Nested, Boolean, analyzer, Completion, Keyword, Text, Integer
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])


# 注意集成DocType
class ArticleType(DocType):
    title = Text(analyzer="ik_max_word")
    # 不需要分词,定义成keyword
    detail_url = Keyword()
    content = Text(analyzer="ik_max_word")
    grep_time = Date()

    class Meta:
        index = "jobbole"
        doc_type = "article"


if __name__ == '__main__':
    ArticleType.init()