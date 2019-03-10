#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute

execute("scrapy crawl quotes -o quotes-humor.json -a tag=zhangshanbo".split(" "))