import scrapy
from quotes_parser.items import ScrapyQuoteItem, ScrapyAuthorItem

authors =[]


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def compose_quote(self, raw_quote):

        quote = ScrapyQuoteItem()
        quote['tags'] = raw_quote.xpath("div[@class='tags']/a/text()").getall()
        quote['author'] = raw_quote.xpath("span/small[@class='author']/text()").get()
        quote['quote'] = raw_quote.xpath("span[@class='text']/text()").get()

        return quote

    def parse(self, response):
        quotes = response.xpath("/html//div[@class='quote']")

        for quote in quotes:
            yield self.compose_quote(quote)
            
        next_page = response.xpath("//li[@class='next']/a/@href").get()

        if next_page is not None:
            yield scrapy.Request(url=self.start_urls[0] + next_page)



class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def compose_author(self, raw_author):

        author = ScrapyAuthorItem()
        author['fullname'] = raw_author.xpath("div[@class='tags']/a/text()").getall()
        author['born_date'] = raw_author.xpath("span/small[@class='author']/text()").get()
        # author['born_location'] = raw_author.xpath("span[@class='text']/text()").get()
        author['description'] = raw_author.xpath("span[@class='text']/text()").get()

        return author

    def parse(self):
        for author in authors:
            yield self.compose_author(author)

   
