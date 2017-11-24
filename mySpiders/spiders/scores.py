import scrapy

class Scores(scrapy.Spider):
    name = "scores"
    start_urls = [
            'http://www.laxpower.com/update17/binboy/XDBNPA.PHP',
    ]

    def parse(self, response):
        for scores in response.css("td.left"):
            yield {
                "team": response.css("title::text").extract_first(),
                # no "dates": response.css("td.left::text").re(r'Date'),
                # no "opponent": response.css("td.left::text").re(r'Opponent'),
                "result": response.css("td.score::text")[0].extract(),
                "dbs": response.css("td.score::text")[1].extract(),
                "dbos": response.css("td.score::text")[2].extract(),
                }
        #filename = 'dumped.log'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)
