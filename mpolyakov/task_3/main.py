import argparse
import json
import os
import requests
from collections import Counter, OrderedDict

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
    '--script-mode',
    default='single',
    choices=('single', 'threaded'),
    help='Script run mode',
)
parser.add_argument(
    '--threads-count',
    default='10',
    help='Count of threads (if threaded mode)',
)


def single_load():
    data = ''
    for url in URL_TO_SAVE:
        response = requests.get(url)
        data += response.text
    return data


def letter_count(data):
    letter_count = dict(Counter(data))
    sorted_letter_count = OrderedDict(
        sorted(letter_count.items(), key=lambda kv: kv[1], reverse=True)
    )
    return sorted_letter_count


def save_to_file(sorted_letter_count, file_name):
    with open(file_name, 'w', encoding='utf8') as json_file:
        json.dump(sorted_letter_count, json_file, ensure_ascii=False, indent=4)


def main():
    args = parser.parse_args()
    save_to_file(letter_count(single_load()), file_name=args.output_file_name)


if __name__ == '__main__':
    main()
