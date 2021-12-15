
from itertools import groupby
from urllib.request import urlopen
from json import loads
from datetime import datetime

def convert_date(date):
    return datetime.strptime(date['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()

def get_edits(edits):
    for key, items in groupby(edits, key=convert_date):
        sum_items = sum(1 for i in items)
        print(key, sum_items)


def main():
    url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
    data = loads(urlopen(url).read().decode('utf8'))
    edits = data['query']['pages']['183903']['revisions']

    get_edits(edits)

if __name__ == '__main__':
    main()
