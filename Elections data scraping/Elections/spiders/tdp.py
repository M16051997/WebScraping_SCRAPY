import scrapy

class ElectionFundsSpider(scrapy.Spider):
    name = "Elections"
    start_urls = ["https://myneta.info/party/index.php?action=all_donors&id=8"]

    def parse(self, response):
        # Assuming the table you want to scrape is the first table on the page
        table = response.xpath("//table[1]")

        # Extract table headers
        headers = table.xpath(".//th/text()").getall()

        # Extract table rows
        rows = table.xpath(".//tr")

        for row in rows[1:]:  # Skip the header row
            # Extract data from each row
            data = row.xpath(".//td/text()").getall()

            # Create a dictionary with headers as keys and row data as values
            row_data = dict(zip(headers, data))

            yield row_data