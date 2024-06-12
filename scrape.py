from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.patreon.com/coreyms').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find('article'):

  headline = article.h2.a.text
  print(headline)

  summary = article.find('div', class_='emtry-content').p.text
  print(summary)

  vid_src = article.find('iframe', class_='youtube-player')['src']

  vid_id = vid_src.split('/')[4]
  yt_link = f'https://youtube.com/watch?v={vid_id}'

