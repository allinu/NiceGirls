from unicodedata import category
import scrapy
from NiceGirls.items import NiceGirlsItem

class VmgirlsSpider(scrapy.Spider):
    name = 'vmgirls'
    allowed_domains = ['www.vmgirls.com']
    start_urls = ['https://www.vmgirls.com/archives.html']

    def parse(self, response):
        page_links = response.xpath('//*[@id="archives"]/ul/li/ul/li/a/@href').extract()
        for link in page_links:
            yield scrapy.Request(link, callback=self.parse_page)

    def parse_page(self, response):
        item = NiceGirlsItem()
        page_name = response.css('title::text').get()
        image_links = response.xpath('/html/body/main/div/div[2]/div[1]/div/div/div[2]/div[3]/p/img/@src').extract()
        category_name = response.xpath('/html/body/main/div/div[2]/div[1]/div/div/div[2]/div[4]/span/a/text()').extract()
        category_name = ' '.join(category_name)
        for link in image_links:
            item['site_name'] = 'vmgirls.com'
            item['category_name'] = category_name
            page_name = page_name.split('丨')[0]
            page_name = str(page_name).strip()
            item['page_name'] = page_name
            item['image_link'] = link
            self.logger.info(f"{page_name} - {link}")
            yield item
