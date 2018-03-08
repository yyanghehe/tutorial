# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    start_urls = [
        "http://v.qq.com/x/list/tv?&offset=0"
    ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        # 	f.write(response.body)

        selector = Selector(response)
        audios = response.xpath('//ul[@class="figures_list"]/li')
        for audio in audios:
            item = DmozItem()
            item['title'] = audio.xpath('div[@class="figure_title_score"]/strong/a/text()').extract()
            item['link'] = audio.xpath('div[@class="figure_title_score"]/strong/a/@href').extract()
            scores = audio.xpath('div[@class="figure_title_score"]/div[@class="figure_score"]/em/text()').extract()
            item["count"] = audio.xpath('div[@class="figure_count"]/span/text()').extract()
            score = ""
            for t in scores:
                score+=t
            item['score'] = score
            # yield item
            print 'title:%s'%item['title'][0].encode('UTF-8')
            print 'scores:%s'%item['score'].encode('UTF-8')
            print 'count:%s'%item["count"][0].encode('UTF-8')
            print 'link:%s'%item['link'][0].encode('UTF-8')