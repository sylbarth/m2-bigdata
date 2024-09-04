import pandas as pd
import feedparser


def get_rss(url):
    feed = feedparser.parse(url)
    posts = []
    for post in feed.entries:
        posts.append((post.id, post.title, post.link, post.summary, post.published_parsed))
    return pd.DataFrame(posts, columns=['id', 'title', 'link', 'summary', 'published_parsed'])


articles = get_rss("https://feeds.a.dj.com/rss/RSSOpinion.xml")

print(articles)
