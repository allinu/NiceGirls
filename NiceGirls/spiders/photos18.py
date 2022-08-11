import scrapy
from NiceGirls.items import NiceGirlsItem


class Photos18Spider(scrapy.Spider):
    name = 'photos18'
    allowed_domains = ['photos18.com']
    start_urls = ['http://www.photos18.com']

    def parse(self, response):
        category_names = response.xpath(
            '//*[@id="w3"]/li/a/p/text()').extract()
        category_links = response.xpath('//*[@id="w3"]/li/a/@href').extract()
        for i in range(0, 17):
            self.logger.info(
                f"{category_names[i]} - {self.start_urls[0] + category_links[i]}"
            )
            yield scrapy.Request(self.start_urls[0] + category_links[i],
                                 callback=self.parse_1)

    def parse_1(self, response):
        collections_list = response.xpath(
            '//*[@id="videos"]/div/div[2]/a/text()')
        collections_link_list = response.xpath(
            '//*[@id="videos"]/div/div[2]/a/@href')
        for i in range(100):
            collection_name = collections_list[i].extract()
            collection_link = self.start_urls[0] + collections_link_list[
                i].extract()
            self.logger.info(f"{collection_name} - {collection_link}")
            yield scrapy.Request(collection_link, callback=self.parse_2)

        next_page = response.xpath(
            '//*[@id="w0"]/ul/li[7]/a/@href').extract_first()
        next_page = self.start_urls[0] + next_page

        yield scrapy.Request(next_page, callback=self.parse_1)

    def parse_2(self, response):
        item = NiceGirlsItem()
        category_name = response.xpath(
            '//*[@id="w4"]/li[2]/a/text()').extract_first()
        page_name = response.css('title::text').get()
        image_links = response.xpath(
            '//*[@id="content"]/div/a/img/@data-src').extract()
        for image_link in image_links:
            item['site_name'] = 'photos18.com'
            item['category_name'] = category_name
            item["page_name"] = page_name
            image_link = str(image_link).split("?")[0]
            item["image_link"] = image_link
            self.logger.info(f"{page_name} - {image_link}")
            yield item
