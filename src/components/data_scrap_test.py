import snscrape.modules.twitter as twitterScraper

scraper = twitterScraper.TwitterUsersScraper("zoho", False)

for i, tweet in enumerate(scraper.get_items()):
    if i >2:
       break
    print(f'{i} content: {tweet.content}')
