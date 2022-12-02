import scrapy
from NiceGirls.items import NiceGirlsItem


class NicegirlSpider(scrapy.Spider):
    name = 'nicegirl'
    allowed_domains = ['nicegirl.in']
    start_urls = ['https://nicegirl.in/archives/']

    def parse(self, response):
        next_page = response.xpath(
            '//div[@class="pagination-next"]/a/@href').extract()[0]
        list_links = response.xpath(
            '/html/body/section/div/div/div[1]/div/div/div/article/div/p[2]/a/@href'
        ).extract()
        for link in list_links:
            _link = str(link).split('.')[0]
            yield scrapy.Request("https://nicegirl.in" + _link,
                                 callback=self.parse_page)
        if (next_page):
            yield scrapy.Request("https://nicegirl.in" + next_page,
                                 callback=self.parse)

    def parse_page(self, response):
        item = NiceGirlsItem()
        page_name = response.xpath(
            '//h1[contains(@class, "title")]/text()').extract()[0]
        image_links = response.xpath(
            '//img[contains(@src, "https:") and contains(@src, "jpg")]/@src').extract()
        category_name = ""
        for link in image_links:
            item['site_name'] = 'nicegirl.in'
            item['category_name'] = category_name
            page_name = page_name.split('丨')[0]
            page_name = str(page_name).strip()
            item['page_name'] = page_name
            item['image_link'] = link
            self.logger.info(f"{page_name} - {link}")
            yield item
