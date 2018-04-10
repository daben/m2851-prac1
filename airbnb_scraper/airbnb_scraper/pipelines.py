# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class DuplicatesPipeline(object):
    def __init__(self):
        super(DuplicatesPipeline, self).__init__()
        self.items_seen = set()

    def process_item(self, item, spider):
        item_id = item['_id']
        # Drop duplicated items
        if item_id in self.items_seen:
            raise DropItem(f"duplicated item {item_id}")

        self.items_seen.add(item_id)
        return item
