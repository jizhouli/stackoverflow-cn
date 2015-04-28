#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
stackoverflow tags 信息摘要抓取
http://stackoverflow.com/tags
http://stackoverflow.com/tags?page=[1..1191]&tab=popular
'''

import scrapy

# HTML DOM PARSE
from scrapy.selector import Selector

from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from scrapy import log

from tagspider.items import TagspiderItem

class TagSpider(CrawlSpider):
    name = 'stackoverflow'
    allowed_domains = ['stackoverflow.com']
    base_url = 'http://stackoverflow.com'

    wiki_page_url = 'http://stackoverflow.com/tags/%s/info'

    def start_requests(self):
        requests = []
        log.start('./stackoverflow.log')

        req = Request(
                url = 'http://stackoverflow.com/tags',

                headers = {
                    'Host': 'stackoverflow.com',
                    'Referer': 'http://stackoverflow.com/tags',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
                    }
                )
        req.meta['detail_page_url'] = 'http://stackoverflow.com/tags?page=%s&tab=popular'
        requests.append(req)

        return requests

    # 解析总页数，生成详情页地址队列
    def parse(self, response):
        log.msg('parse list page: %s' % str(response))

        selector = Selector(response=response)
        last_pager = selector.xpath("//div[@class='pager fr']//a[last()-1]/span/text()").extract()[0]
        log.msg("get total page num: %s" % last_pager)

        #TODO
        last_pager = 100

        detail_page_url = response.request.meta['detail_page_url']
        for pager in range(1, last_pager+1):
            url = detail_page_url % pager
            yield Request(url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        log.msg('parse detail page: %s' % str(response))

        selector = Selector(response=response)
        tag_nodes = selector.xpath("//td[@class='tag-cell']")
        for tag in tag_nodes:
            name = tag.xpath("./a/text()").extract()[0]
            sum = tag.xpath(".//span[@class='item-multiplier-count']/text()").extract()[0]
            excerpt = tag.xpath(".//div[@class='excerpt']/text()").extract()[0]

            href = tag.xpath("./a/@href").extract()[0]
            feature = href.split('/')[-1]
            detail_page_url = self.wiki_page_url % feature

            req = Request(
                    url = detail_page_url,
                    callback = self.parse_wiki_page,
                    )
            req.meta['name'] = name
            req.meta['sum'] = sum
            req.meta['excerpt'] = excerpt
            yield req

        # end for-loop

    def parse_wiki_page(self, response):
        log.msg('parse wiki page: %s' % str(response))

        selector = Selector(response=response)
        excerpt = selector.xpath("//div[@id='wiki-excerpt']/p/text()").extract()[0]
        wiki = selector.xpath("//div[@class='post-text']").extract()[0]
        #log.msg(excerpt)
        #log.msg(wiki)

        item = TagspiderItem()
        item['name'] = response.request.meta['name']
        item['sum'] = response.request.meta['sum']
        item['excerpt'] = excerpt
        item['wiki'] = wiki

        return item

