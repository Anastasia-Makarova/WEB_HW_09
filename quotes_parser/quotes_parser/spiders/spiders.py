import scrapy
from quotes_parser.items import ScrapyQuoteItem
import json

authors = []

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def compose_quote(self, raw_quote):

        quote = ScrapyQuoteItem()
        quote['tags'] = raw_quote.xpath("div[@class='tags']/a/text()").getall()
        quote['author'] = raw_quote.xpath("span/small[@class='author']/text()").get()
        # quote['link'] = raw_quote.xpath("span[2]/a/@href").get() 
        quote['quote'] = raw_quote.xpath("span[@class='text']/text()").get()

        return quote

    def parse(self, response):
        quotes = response.xpath("/html//div[@class='quote']")

        for quote in quotes:
            # authors.append(quote.xpath("span[2]/a/@href").get())
            link =f'https://quotes.toscrape.com{quote.xpath("span[2]/a/@href").get()}'
            if link not in authors:
                authors.append(link)
            yield self.compose_quote(quote)

        next_page = response.xpath("//li[@class='next']/a/@href").get()

        if next_page is not None:
            yield scrapy.Request(url=self.start_urls[0] + next_page)
        else:
            with  open ('authors_links.json', 'a') as file:
                        json.dump(authors, file)


   
