# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NiceGirlsItem(scrapy.Item):
    site_name = scrapy.Field()
    category_name = scrapy.Field()
    page_name = scrapy.Field()
    image_link = scrapy.Field()
