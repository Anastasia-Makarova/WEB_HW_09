# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyQuoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    tags = scrapy.Field()
    author = scrapy.Field()
    quote = scrapy.Field()


class ScrapyAuthorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    fullname = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
    description = scrapy.Field()
