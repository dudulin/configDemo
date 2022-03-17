# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

"""
功能
1.下载中间件 --------- 通常下 编写 下载器中间件
2.爬虫中间件

2.1 随机使用 USER　AGENT  --2.2　代理ip  --2.3 slenium配合使用 

中间件：预处理 request 和 response 对象
1.对header 以及 cookie 进行更换和处理
2.使用代理ip等
3.对请求进行定制化操作
"""
import random

from demoConfig.settings import USER_AGENT_LIST, IP_LIST


class RandomUserAgent(object):

    # * 请求默认执行 函数 1. 修改请求头的 user agent
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        proxy = random.choice(IP_LIST)

        # * 修改 浏览器版本 防 封IP
        request.headers['User-Agent'] = user_agent
        request.meta['proxy'] = proxy['ip']

        print(request.meta['proxy'], request.headers['User-Agent'], '代理ip')

        # return None  # 没有return 一样表示返回 None
        # 返回3种类型 ，处理 方法都不一样
        # None   request 传递给 下载器 或者 下一个权重 低的 process_request
        # Request   request对象 通过引起 交给 调度器
        # Response   不再请求， 把 response 返回给引擎 --- 不联 下载器 和  intent ---交给 spider 进行解析


class RandomIp(object):

    def process_request(self, request, spider):
        # 免费IP 经常卡死
        proxy = random.choice(IP_LIST)
        http = request.url.split('://')[0]
        if 'user_password' in proxy:
            # 对账户密码进行编译
            b64_up = base64.b64encode(proxy['user_password'].encode())
            # 设置认证
            request.headers['Proxy-Authorization'] = 'Basic ' + b64_up.decode()
            # 设置代理
            request.meta['proxy'] = proxy['ip']
        else:
            request.meta['proxy'] = proxy['ip']
            print(request.meta['proxy'], '代理ip', http)

        return None
