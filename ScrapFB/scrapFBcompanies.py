#pip install facebook-scraper

from facebook_scraper import get_posts
for post in get_posts('tiendamanzanita', pages=7):
    #print(post)
    #print(post['time'])
    print(post['text'])