# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy.http import Request

class NiceGirlsPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("images.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_name TEXT,
            category_name TEXT,
            page_name TEXT,
            image_link TEXT UNIQUE
        )""")
        return spider

    def process_item(self, item, spider):
        try:
            self.cur.execute("""INSERT INTO images (site_name, category_name, page_name, image_link)
                VALUES (?, ?, ?, ?)""", (item["site_name"], item["category_name"], item["page_name"], item["image_link"]))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass
        return item

    def close_spider(self, spider):
        self.conn.close()
        return spider

class NiceGirlsDownloaderPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['image_link'])

    def file_path(self, request, item, response=None, info=None):
        image_name = request.url.split('/')[-1]
        image_name = os.path.join(item['site_name'], item['category_name'], item['page_name'],image_name)
        return image_name
