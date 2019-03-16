# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from back_spiders.items import JobBoleItem
import datetime
import re


class JobboleSpider(RedisSpider):
    name = 'jobbole'
    start_urls = ['http://blog.jobbole.com/all-posts/']
    redis_key = "jobbole:strat_urls"

    def parse(self, response):
        # 获取最大页数
        all_page_num = response.xpath("//div[@class='navigation margin-20']//a/text()")[-2].extract()

        all_url = response.xpath("//div[@id='archive']//a[@class='archive-title']/@href").extract()
        for url in all_url:
            yield Request(url=url, callback=self.parse_parse_detail)

        base_url = "http://blog.jobbole.com/all-posts/page/{}/"
        for page in range(2, int(all_page_num) + 1):
            url = base_url.format(page)
            yield Request(url=url, callback=self.parse_list)

    def parse_list(self, response):
        all_url = response.xpath("//div[@id='archive']//a[@class='archive-title']/@href").extract()
        for url in all_url:
            yield Request(url=url, callback=self.parse_parse_detail)

    def parse_parse_detail(self, response):
        title = response.xpath("//div[@class='entry-header']/h1/text()").extract_first()
        content_with_blank = "".join(response.xpath("//div[@class='entry']//text()").extract())
        content = re.sub("\s", "", content_with_blank)
        jobboleItem = JobBoleItem()
        jobboleItem['title'] = title
        jobboleItem['detail_url'] = response.url
        jobboleItem['content'] = content
        jobboleItem['grep_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yield jobboleItem