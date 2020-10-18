import argparse
import json
import threading
import time
from collections import Counter
from pathlib import Path

import requests
from progress.bar import Bar

URL_TO_SAVE = (
    'https://en.wikipedia.org/wiki/Wikipedia',
    'https://en.wikipedia.org/wiki/Main_Page',
    'https://en.wikipedia.org/wiki/COVID-19_pandemic',
    'https://ru.wikipedia.org/wiki/Пандемия_COVID-19',
    'https://yi.wikipedia.org/wiki/קאוויד-19_פאנדעמיק',
    'https://tr.wikipedia.org/wiki/COVID-19_pandemisi',
    'https://uk.wikipedia.org/wiki/Пандемія_коронавірусної_хвороби_2019',
    'https://bg.wikipedia.org/wiki/Пандемия_от_коронавирус_(2019_–_2020)',
    'https://be.wikipedia.org/wiki/Пандэмія_COVID-19',
    'https://ro.wikipedia.org/wiki/Pandemia_de_coronaviroză_(COVID-19)'
)


parser = argparse.ArgumentParser()
parser.add_argument(
    '--output_file_name',
    default='/var/tmp/output.json',
    help='Path to the outputfile in JSON format',
)
parser.add_argument(
    '--script_mode',
    default='single',
    choices=('single', 'threaded'),
    help='Script run mode',
)
parser.add_argument(
    '--threads_count',
    default=2,
    help='Count of threads (if threaded mode)',
)


def load(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
        requests.exceptions.RequestException,
    ) as exc:
        print('An error occurred: %s', exc)
    return str(response.content)


def single_load(urls):
    data = ''
    bar = Bar('Processing', max=len(URL_TO_SAVE))
    for url in urls:
        data += load(url)
        bar.next()
        print(' ', url)
    bar.finish()
    print('Total letters quantity: {}'.format(len(data)))
    return data


DATA = ''
lock = threading.Lock()


def t_load(urls):
    global DATA
    for url in urls:
        with lock:
            DATA += load(url)


def threading_load(urls, threads_count):
    for i in range(threads_count):
        start = i * len(urls) // threads_count
        stop = (i+1) * len(urls) // threads_count
        thread = threading.Thread(target=t_load, args=(urls[start:stop],))
        thread.start()
        print(thread.name)
        thread.join()
    print('Total letters quantity: {}'.format(len(DATA)))
    return DATA


def letter_count(data):
    letter_count = dict(Counter(data))
    sorted_letter_count = dict(
        sorted(letter_count.items(), key=lambda x: x[1], reverse=True))
    return sorted_letter_count


def save_to_file(sorted_letter_count, file_name):
    p = Path(file_name)
    with p.open('w', encoding='utf8') as file:
        json.dump(sorted_letter_count, file,
                  ensure_ascii=False, indent=4)


def main():
    start_time = time.time()
    args = parser.parse_args()
    if args.script_mode == 'threaded':
        save_to_file(letter_count(
            threading_load(URL_TO_SAVE, int(args.threads_count))),
            file_name=args.output_file_name)
    else:
        save_to_file(letter_count(
            single_load(urls=URL_TO_SAVE)),
            file_name=args.output_file_name)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
