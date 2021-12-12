import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def parse_news(channel):
    news = []
    for elem in channel.findall('item'):
        news.append({'pubDate': elem.find('pubDate').text, 'title': elem.find('title').text})
    return news


def parse_all_news(channel):
    news = []
    tags = {}
    for elem in channel.findall('item'):
        for counter in elem:
            tags[counter.tag] = counter.text
    news.append(tags)
    return news


def save_json(channel, file_name):
    news_file = json.dumps(channel, ensure_ascii=False, indent=4).encode('utf8')
    with open(file_name, 'wb') as file:
        file.write(news_file)


def main():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    print(parse_all_news(root[0]))
    save_json(parse_all_news(root[0]), 'news')

if __name__ == '__main__':
    main()
