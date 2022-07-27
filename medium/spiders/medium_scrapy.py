from datetime import datetime, timezone
import scrapy
from ..items import MediumItem
from ..pipelines import MediumPipeline
 


class MediumscrapySpider(scrapy.Spider):
    """
    Medium Scraper
    """
    name = 'mediumscrapy'
    # allowed_domains = ['https://medium.com']
    start_urls = [
        
    ]

    def __init__(self, *args, **kwargs):
        super(MediumscrapySpider, self).__init__(*args, **kwargs)  # <- important
        self.category = kwargs.get("category", None)
        self.url = "https://medium.com/"
        if self.category:
            self.url = self.url + "tag/"+ self.category 
        self.start_urls.append(self.url)
        

        
    
         
    def parse(self, response):
        # response : contains the html source code
        self.items = MediumItem()
        all_articles = response.css('article.meteredContent')
        for article in all_articles:
            author = article.css('p::text').get()
            title = article.css('h2::text').get()
            summary = article.css('div.h').css('p::text').get()
            self.items['author'] = author
            self.items['title'] = title
            self.items['summary'] = summary
        

            yield self.items  # everytime item is scraped and seding to the pipelines

        