# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MediumItem(scrapy.Item):
    # define the fields for your item here like:
    author= scrapy.Field()
    title = scrapy.Field()
    summary = scrapy.Field()
    # published_date = scrapy.Field()
    article_link = scrapy.Field()

    
