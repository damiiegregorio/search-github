import requests
import argparse
import getpass
from datetime import datetime
import csv


def login(username, word):
    pwd = getpass.getpass()
    r = requests.get('https://api.github.com/users', auth=(username, pwd))
    if r.status_code == 200:
        search(word)
        # csv_file(word)
    else:
        print('Authentication failed.')


def search(word):
    list_comprehension = [i for i in range(1, 10)]

    for page in list_comprehension:
        payload = {'q': word, 'sort': 'stars', 'order': 'des', 'page': page, 'per_page': 100}
        search_word = requests.get('https://api.github.com/search/repositories', params=payload)
        data = search_word.json()
        items = data['items']

        for item in items:
            name = item['name']
            des = item['description']
            url = item['html_url']
            language = item['language']
            update = item['updated_at']

            result = [name, des, url, language, update]
            # result = {'name': name, 'description': des, 'url': url, 'language': language, 'date': update}
            # return result
            csv_file(result)


def date_formatter():
    today = datetime.now().strftime("-%Y-%m-%d-%H-%M")
    date_today = "output" + today
    return date_today


def csv_file(result):
    date_today = date_formatter()

    with open(date_today + ".csv", 'a', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file, lineterminator='\r')
        writer.writerow(['Name', 'Description', 'URL', 'Language', 'Date'])
        writer.writerow(result)


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--username', type=str, help='Enter username')
        parser.add_argument('word', type=str, help='Enter keyword')

        args = parser.parse_args()
        login(args.username, args.word)

    except IndexError:
        print('Error')


if __name__ == '__main__':
    main()