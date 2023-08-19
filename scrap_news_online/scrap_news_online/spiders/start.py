import scrapy


class ScrapOnline(scrapy.Spider):
    name = "scrap_news_online"
    start_urls = ["https://www.thehindu.com/topic/russia-ukraine-crisis/"]

    def parse(self, response):
        titles = response.xpath('//h3[@class="title big"]/a/text()').getall()
        for title in titles:
            yield {
                'title': title.strip()
            }
    ## If page have show more button

    ### Find the "Show More" button and submit the form to load more data

        show_more_button = response.css('.SHOW MORE')
        if show_more_button:
            formdata = {'pageajax': 'true'}
            yield FormRequest.from_response(
                response,
                formdata=formdata,
                callback=self.parse_more_data
            )
    
        def parse_more_data(self, response):
            # Extract additional data loaded after clicking "Show More"
            titles = response.xpath('//h3[@class="title big"]/a/text()').getall()
            for title in titles:
                yield {
                    'title': title.strip()
                }