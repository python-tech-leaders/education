import os
import time
from operator import itemgetter
import argparse
from downloader import get_data_by_single_thread, get_data_by_more_thread
from counter import count_char

urls = [
    'https://en.wikipedia.org/wiki/Wikipedia',
    'https://en.wikipedia.org/wiki/Main_Page',
    'https://en.wikipedia.org/wiki/COVID-19_pandemic',
    'https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BD%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F_COVID-19',
    'https://yi.wikipedia.org/wiki/%D7%A7%D7%90%D7%95%D7%95%D7%99%D7%93-19_%D7%A4%D7%90%D7%A0%D7%93%D7%A2%D7%9E%D7%99%D7%A7',
    'https://tr.wikipedia.org/wiki/COVID-19_pandemisi',
    'https://uk.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BD%D0%B4%D0%B5%D0%BC%D1%96%D1%8F_%D0%BA%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D1%96%D1%80%D1%83%D1%81%D0%BD%D0%BE%D1%97_%D1%85%D0%B2%D0%BE%D1%80%D0%BE%D0%B1%D0%B8_2019',
    'https://bg.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BD%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F_%D0%BE%D1%82_%D0%BA%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81_(2019_%E2%80%93_2020)',
    'https://be.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BD%D0%B4%D1%8D%D0%BC%D1%96%D1%8F_COVID-19',
    'https://ro.wikipedia.org/wiki/Pandemia_de_coronaviroz%C4%83_(COVID-19)'
]

DIR = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    print('Please wait...')
    parser = argparse.ArgumentParser(description='Created by Aurel.VU for Education course DataArt')
    parser.add_argument("--output-file-name", type=str, default='output.txt', help='Path to the output file')
    parser.add_argument("--script_mode", type=str, choices=["threaded", "single"], default='single',
                        help='Script run mode')
    parser.add_argument("--threads_count", type=int, default=4, help='Count of thread (if threaded mode)')
    args = parser.parse_args()

    start_time = time.time()
    if args.script_mode == 'single':
        data = get_data_by_single_thread(urls)
    elif args.script_mode == 'threaded':
        data = get_data_by_more_thread(urls, args.threads_count)
    else:
        raise Exception('Incorrect mode')

    path = os.path.join(DIR, args.output_file_name)
    result = {}
    urls_iter = iter(urls)
    for text in data:
        text_form = str(dict(sorted(count_char(text).items(), key=itemgetter(1), reverse=True))).replace(', ', '\n')[
                    1:-1]
        url = next(urls_iter)
        result[url] = text_form
    finish_time = time.time()
    del urls_iter

    with open(path, "w", encoding="utf-8") as file:
        for url, text_form in result.items():
            file.write(f"URL: {url} \n\n{text_form}\n\n\n")

    print(f'Work is done. Result is saved in file {path}. '
          f'Time duration of processing is {finish_time - start_time} seconds')
