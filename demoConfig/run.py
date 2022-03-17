from scrapy import cmdline

cmdline.execute('scrapy crawl demo -o title.json'.split())  # --nolog  不打印
