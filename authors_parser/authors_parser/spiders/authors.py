from typing import Iterable
import scrapy
from scrapy.http import Request
from pathlib import Path
from authors_parser.items import  ScrapyAuthorItem
import json


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    # current_directory = Path.cwd()
    # file_path = current_directory.parents[1].joinpath('quotes_parser/quotes_parser/authors_links.json')
    # with open (file_path, 'r') as file:
    #         start_urls = file.read()
    

    def start_requests(self) -> Iterable[Request]:
        current_directory = Path.cwd()
        file_path = current_directory.parents[1].joinpath('quotes_parser/quotes_parser/authors_links.json')
        
        with open (file_path, 'r') as file:
            content = json.loads(file_path.read_text())

        for url in content:
            yield Request(url)
    #     # return super().start_requests()

    def compose_author(self, raw_author):

        author = ScrapyAuthorItem()
        author['fullname'] = raw_author.xpath("h3[@class='author-title']/text()").get()
        author['born_date'] = raw_author.xpath("p/span[@class='author-born-date']/text()").get()
        author['born_location'] = raw_author.xpath("p/span[@class='author-born-location']/text()").get()
        author['description'] = raw_author.xpath("div[@class='author-description']/text()").get()

        return author

    def parse(self, response):
        author = response.xpath("/html//div[@class='author-details']")
        yield self.compose_author(author)
