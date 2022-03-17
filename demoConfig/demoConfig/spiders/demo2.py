import scrapy
from ..items import DemoconfigItem
from demoConfig.settings import IP_LIST
import requests

"""
备注：* 表示命名是固定的 不能随意修改 内置的变量 --- 不去写代码执行，模板自动回去读取 运行
功能 
1.返回数据加工 之后发送给 管道 pipelin
2.设置翻页读取数据
"""


class DemoSpider(scrapy.Spider):
    name = 'demo2'
    # * 允许执行的 域名  allowed_domains需要是域名，而不是 urls
    allowed_domains = ['movie.douban.com']

    # * 初始 运行的链接
    start_urls = ['https://movie.douban.com/top250']

    # * 请求返回的 响应 执行函数 1.返回数据加工 之后发送给 管道 pipelin
    def parse(self, response):
        # 这时候获取到的对象 是 节点 对象
        print('123')
        lists = response.xpath('//div[@class="hd"]')
        print(list, 'list')
        for i in lists:
            # 构造item 必须在 for 循环中
            item = DemoconfigItem()
            # item后面的属性 必须在 items.py 文件构造过的 属性
            item['title'] = i.xpath('.//a/span[1]//text()').get()  # get() 吧节点对象变成 字符串
            # * yield 把权限交付给管道处理
            print(item, 'sss')
            yield item
