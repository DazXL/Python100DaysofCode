# getting a live html using beautiful soup documentation in: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup # importing beautiful soup 4
import requests

response = requests.get("https://news.ycombinator.com/news") #gets the html of the page as text

#using beautifulSoup to scrape titles and links to news in that webpage
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
article_texts = []
article_links = []
article_upvotes = []
articles = soup.find_all(name="span", class_="titleline")

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.a["href"]
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

highest_upvote = article_upvotes.index(max(article_upvotes))
print(highest_upvote)
highest_upvotes = article_texts[highest_upvote] + ' ' + article_links[highest_upvote]
print(highest_upvotes)