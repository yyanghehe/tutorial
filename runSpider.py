from scrapy import cmdline

cmdline.execute('scrapy crawl quotes -o quotes-humor.json -a tag=humor'.split())