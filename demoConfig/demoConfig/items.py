# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
"""
功能
1.设置 spider中 收集的键值对
"""

class DemoconfigItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
