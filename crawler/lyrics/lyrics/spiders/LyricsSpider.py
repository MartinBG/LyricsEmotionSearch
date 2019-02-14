import scrapy
import string
import json
from pprint import pprint

class QuotesSpider(scrapy.Spider):
    name = "lyrics"
    start_urls = [
        'http://www.azlyricdb.com/browse/a',
        'http://www.azlyricdb.com/browse/b',
        'http://www.azlyricdb.com/browse/c',
        'http://www.azlyricdb.com/browse/e',
        'http://www.azlyricdb.com/browse/f',
        'http://www.azlyricdb.com/browse/g',
        'http://www.azlyricdb.com/browse/h',
        'http://www.azlyricdb.com/browse/i',
        'http://www.azlyricdb.com/browse/j',
        'http://www.azlyricdb.com/browse/k',
        'http://www.azlyricdb.com/browse/l',
        'http://www.azlyricdb.com/browse/m',
        'http://www.azlyricdb.com/browse/n',
        'http://www.azlyricdb.com/browse/o',
        'http://www.azlyricdb.com/browse/p',
        'http://www.azlyricdb.com/browse/q',
        'http://www.azlyricdb.com/browse/r',
        'http://www.azlyricdb.com/browse/s',
        'http://www.azlyricdb.com/browse/t',
        'http://www.azlyricdb.com/browse/u',
        'http://www.azlyricdb.com/browse/v',
        'http://www.azlyricdb.com/browse/w',
        'http://www.azlyricdb.com/browse/x',
        'http://www.azlyricdb.com/browse/y',
        'http://www.azlyricdb.com/browse/z',
        'http://www.azlyricdb.com/browse/19'
    ]

    def parse(self, response):
        base_url='http://www.azlyricdb.com'
        split = response.url.split('/')
        state = split[-2]
        specific = split[-1]
        if(state == 'browse'):
            all_res = response.css('td a::attr(href)').getall()
            all_res = [x for x in all_res if len(x.split('/')) > 2]
            with open('artists/' + specific + '.json', 'w') as out:
                json.dump(all_res, out, indent = 4)
            for x in all_res:
                next_page = base_url + x
                yield response.follow(next_page, callback=self.parse)
        if(state == 'artist'):
            all_res = response.css('td a::attr(href)').getall()
            all_res = [x for x in all_res if len(x.split('/')) > 2]
            with open('songs/' + specific + '.json', 'w') as out:
                json.dump(all_res, out, indent = 4)
            for x in all_res:
                next_page = base_url + x
                yield response.follow(next_page, callback=self.parse)
        if(state == 'lyrics'):
             result = response.xpath("//*[contains(@id, 'lrc')]/li").getall()
             with open('texts/' + specific + '.json', 'w') as out:
                json.dump(result, out, indent = 4)