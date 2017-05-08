# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

class QuotesCrawlerSpider(scrapy.Spider):
    name = "repaso"
    allowed_domains = ["http://quotes.toscrape.com/"]
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        item  = {
            'text': response.css('span.text::text').extract(),
            'author': response.css('.author::text').extract(),
            'keywords': response.css('meta.keywords::attr(content)').extract()
        }

        yield item

        df = pd.DataFrame(item)
        df.to_csv('/Users/user/Desktop/file.csv', index=False, na_rep='NaN')
        print(df)