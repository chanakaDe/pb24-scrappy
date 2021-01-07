import scrapy

class PostsSpider(scrapy.Spider):
    name = "sparhandy"

    start_urls = [
        'https://www.sparhandy.de/apple/'
    ]

    def parse(self, response):
        for post in response.css('.product-list-item'):
            yield {
                'brand': post.css('article header .brand::text').get(),
                'model': post.css('article header .model::text').get(),
                'price': post.css('article footer .price-info p .price-euro::text').get(),
                'cents': post.css('article footer .price-info p .price-cent::text').get(),
            }

 # response.css('.product-list-item article header .model::text').getall()
 # response.css('.product-list-item article footer .price-info p .price-euro').getall()