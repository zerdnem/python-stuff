import scrapy

class ImgurItem(scrapy.Item):
	title = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()


#//settings.py//

BOT_NAME = 'imgur'

SPIDER_MODULES = ['imgur.spiders']
NEWSPIDER_MODULE = 'imgur.spiders'
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = '/home/ubuntu/imgurFront/'


#//imgur_spider.py//

import scrapy

from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors import LinkExtractor
from imgur.items import ImgurItem

class ImgurSpider(CrawlSpider):
	name = 'imgur'
	allowed_domains = ['imgur.com']
	start_urls = ['http://www.imgur.com']
	rules = [Rule(LinkExtractor(allow=['/gallery/.*']), 'parse_imgur')]

	def parse_imgur(self, response):
		image = ImgurItem()
		image['title'] = response.xpath(\
			"//h2[@id='image-title']/text()").extract()
		rel = response.xpath("//img/@src").extract()
		image['image_urls'] = ['http:'+rel[0]]
		return image


#/STAGE 2/

#//pipelines.py//

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline

class ImgurPipeline(ImagesPipeline):

	def set_filename(self, response):
		#add a regex here to check the title is valid for a filename.
		return 'full/{0}.jpg'.format(response.meta['title'][0])

	def get_media_requests(self, item, info):
		for image_url in item['image_urls']:
			yield scrapy.Request(image_url, meta={'title': item['title']})

	def get_images(self, response, request, info):
		for key, image, buf in super(ImgurPipeline, self).get_images(response, request, info):
			key = self.set_filename(response)
		yield key, image, buf

#//settings.py//

ITEM_PIPELINES = {'imgur.pipelines.ImgurPipeline': 1}









