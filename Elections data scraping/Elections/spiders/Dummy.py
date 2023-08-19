import scrapy

class ElectionFundsSpider(scrapy.Spider):
    name = "elections"
    start_urls = ["https://myneta.info/party/index.php?action=all_donors&id=23"]

    def parse(self, response):
        # Assuming the table you want to scrape is the first table on the page
        table = response.xpath("//table[1]")

        # Extract table rows
        rows = table.xpath(".//tr[position() > 1]")  # Exclude the first row (header row)

        for row in rows:
            # Extract data from each row
            columns = row.xpath(".//td")
            data = []

            for column in columns:
                # Extract text content from column
                text = column.xpath(".//text()").get(default='').strip()
                data.append(text)

            yield {
                "data": data
            }
