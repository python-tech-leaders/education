import queue
import sys
import collections
import time
import requests
from pathlib import Path
import threading
import argparse

global all_symbols
all_symbols = ''


parser = argparse.ArgumentParser(description='Incredible parser wiki. It shows count of all symbols from asked wiki '
                                             'http(s) pages.')
parser.add_argument('--output-file-name', type=str, default='symbol_count.txt',
                    help='set name of an output file (default is "symbol_count.txt")')
parser.add_argument('--script-mode', type=str, choices=('single', 'threaded'), default='threaded',
                    help='Script run mode. Values: threaded, single. Default is single')
parser.add_argument('--threads_count', type=int, default=3,
                    help='Set max active threads. Default is 3')

args = parser.parse_args()

links = (
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

# ================ with no threading: ==========================================
def get_symbols_from_link(link: str) -> str:
    """get html from link"""
    result = ''
    try:
        response = requests.get(link)
        response.raise_for_status()
        result = response.text

    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
        requests.exceptions.RequestException,
    ) as exc:
        print('Connection error occurred: %s', exc)
    except Exception as exc:
        print('An error occurred: %s', exc)
    return result


def export_to_file(text, name) -> None:
    """save text to file"""
    output_text = ''
    for key, val in text.items():
        output_text += f'"{key}": {val}\n'  # for vertical view (not in one string)

    outpath = Path.cwd() / name
    outpath.write_text(output_text)



def main_no_threading() -> None:
    # 1) Download all http text with no threading
    all_symbols = ''
    for link in links:
        all_symbols += get_symbols_from_link(link)

    # 2) Check every symbol, and create sorted dict with symbol count
    symbol_count = dict(collections.Counter(all_symbols))

    # 3) export text to file symbol_count.txt
    export_to_file(symbol_count, args.output_file_name)


# ======================with threading:==========================================
def get_symbols_from_link_threaded(link: str):
    """get html from link"""
    global all_symbols

    try:
        response = requests.get(link)
        response.raise_for_status()
        all_symbols += response.text

    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
        requests.exceptions.RequestException,
    ) as exc:
        print('Connection error occurred: %s', exc)
    except Exception as exc:
        print('An error occurred: %s', exc)





def threading_get_symbols_from_link() -> None:
    """work with threading"""
    threads_need = args.threads_count     # I can't make task with quantity of threads =( sorry, guys
    threads = []
    for link in links:
        thread = threading.Thread(target=get_symbols_from_link_threaded, args=(link, ))
        threads.append(thread)

    for next_thread in threads:
        next_thread.start()
        print('thread started ', next_thread)
    for next_thread in threads:
        next_thread.join()


def main_with_threading():
    global all_symbols
    threading_get_symbols_from_link()
    symbol_count = dict(collections.Counter(all_symbols))
    export_to_file(symbol_count, args.output_file_name)


if __name__ == '__main__':
    start_time = time.time()
    if args.script_mode == 'single':
        main_no_threading()
    elif args.script_mode == 'threaded':
        main_with_threading()

    print('Elapsed time: ' + format(time.time() - start_time))
