from django.shortcuts import render
# from django.http import JsonResponse
from django.utils.timezone import now
from .forms import FeedForm
# from scrapy.crawler import CrawlerRunner
# from scrapy import signals
# import crochet

# crochet.setup()

# class ScrapyCrawler:
#     def __init__(self):
        
#         self.runner = CrawlerRunner()
#         self.feeds = []

#     @crochet.wait_for(timeout=60.0)
#     def crawl(self, domain):
#         self.feeds = []
#         dispatcher.connect(self._crawler_result, signal=signals.item_scraped)
#         eventual = self.runner.crawl(FeedSpider, start_urls=[f'http://{domain}'])
#         return eventual

#     def _crawler_result(self, item, response, spider):
#         self.feeds.extend(item['feeds'])

def search_feed(request):
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            domain = form.cleaned_data['domain']
            # Placeholder for future Scrapy integration
            results = ["Feed 1", "Feed 2", "Feed 3","Feed 1", "Feed 2", "Feed 3","Feed 1", "Feed 2", "Feed 3","Feed 1", "Feed 2", "Feed 3","Feed 1", "Feed 2", "Feed 3"]  # Example results; replace with actual results
            
            context = {
                'form': form,
                'results': results,
                'domain': domain,
                'timestamp': now().timestamp()
            }
            return render(request, 'feeds/feedHome.html', context)
    else:
        form = FeedForm()
        
    context = {
        'form': form,
        'results': [],
        'domain': '',
        'timestamp': now().timestamp()
    }
    return render(request, 'feeds/feedHome.html', context)