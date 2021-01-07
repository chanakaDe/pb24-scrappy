import scrapy

class PostsSpider(scrapy.Spider):
    name = "tariff"

    start_urls = [
        'https://www.sparhandy.de/apple/iphone-12/',
    ]

    def parse(self, response):
        for post in response.css('.product-list-item'):
            yield {
                'name': post.css('article header .product-box-header-link .product-box-headline::text').get(),
                'tariff_mlf_main': post.css(
                    'article footer .prices-wrap .price-item .price-item-text .price .price-euro::text').get(),
                'tariff_mlf_cent': post.css(
                    'article footer .prices-wrap .price-item .price-item-text .price .price-cent::text').get(),
                'gerat_einm': post.css(
                    'article footer .prices-wrap .price-item .price-item-text span::attr(content)').get(),
            }
