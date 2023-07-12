import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()
            if 'catalogue/' in relative_url:
                next_page_url = f'https://books.toscrape.com/{relative_url}'
            else:
                next_page_url = f'https://books.toscrape.com/catalogue/{relative_url}'
            yield response.follow(next_page_url,callback=self.parse_book_page)
    

    def parse_book_page(self,response):
        pass