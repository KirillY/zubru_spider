# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClinicItem(scrapy.Item):
    Name = scrapy.Field()
    Working_hrs = scrapy.Field() 
    Address = scrapy.Field()
    Description = scrapy.Field()

class DoctorItem(scrapy.Item):
	
