import scrapy

class Scores(scrapy.Spider):
    name = "lax_scores"
    start_urls = [
            "http://www.laxpower.com/update17/binboy/XDBNPA.PHP",
    ]

    def parse(self, response):
        #for result in response.css('tr'):
        for result in response.css('td'):
            yield {
                'team': response.css('title::text').extract_first(), #ok
                'gamedate': response.css('td.left::text')[3].extract(), #ok
                'opponent': response.css('td.opponent::text').extract(),
                'result': response.css('td.score::text')[0].extract(), #ok
                's1': response.css('td.score::text')[1].extract(), #ok
                's2': response.css('td.score::text')[2].extract(), #ok
                }
            
