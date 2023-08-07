# web-scrapping
fetch('https://books.toscrape.com/')
books = response.css('article.product_prod')

<!-- run -->
scrapy crawl bookspider
<!-- want to save in file -->
scrapy crawl bookspider -0 bookdata.json
fetch('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
table_rows = response.css('table tr')