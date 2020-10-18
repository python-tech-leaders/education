import sys
import time
import requests
from pathlib import Path
import threading
import argparse

parser = argparse.ArgumentParser(description='Incredible parser wiki. It shows count of all symbols from asked wiki http(s) pages.')
parser.add_argument('--output-file-name', type=str, default='symbol_count.txt', help='set name of an output file (default is "symbol_count.txt")')
parser.add_argument('--script-mode', type=str, default="single", help='Script run mode. Values: threaded, single. Default is single')
parser.add_argument('--threads_count', type=bool, default=False, help='Show count of threads. Values: true or false. Default is False')
args = parser.parse_args()

symbol_count = {}
use_threading = False

show_threads = False
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
    try:
        response = requests.get(link)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)

    return response.text


def sort_dict(symbol_count: dict) -> str:
    """sort dict by values
    :return: sorted dict"""
    symbol_count_sorted = ''
    for key, val in sorted(symbol_count.items(), key=lambda x: x[1]):
        symbol_count_sorted += f'"{key}": {val}\n'
    return symbol_count_sorted


def export_to_file(text: str, name) -> None:
    """save text to file symbol_count.txt"""
    outpath = Path.cwd() / name
    outpath.write_text(text)


def main_no_threading() -> None:
    # 1) Download all http text with no threading
    all_symbols = ''
    for link in links:
        all_symbols += get_symbols_from_link(link)

    # 2) Check every symbol, and create dict with symbol (as ) count
    symbol_count = {}
    for symbol in all_symbols:
        try:
            symbol_count[symbol] += 1
        except:
            symbol_count[symbol] = 1

    # 4) Sort dict by values and convert to str:
    symbol_count_sorted = sort_dict(symbol_count)

    # 5) export dit to file symbol_count.txt
    export_to_file(symbol_count_sorted, args.output_file_name)


# ======================with threading:==========================================
def threading_get_symbols_from_link(link: str) -> None:
    """get html from link"""
    global symbol_count


    try:
        response = requests.get(link)   # get text from wiki
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)

    for symbol in response.text:
        try:
            symbol_count[symbol] += 1
        except:
            symbol_count[symbol] = 1


def main_with_threading():
    global symbol_count
    global show_threads

    # 1) Download all http text with threading and create set:
    for link in links:
        thread = threading.Thread(target=threading_get_symbols_from_link, args=(link,))
        thread.start()


    while threading.active_count() > 1:
        if args.threads_count is True:
            act_count = threading.active_count()
            while threading.active_count() == act_count:
                time.sleep(0.01)
            print('Текущее количество активных потоков:', threading.active_count())
        time.sleep(0.01)

    # we have symbol count set. Let's sort it
    symbol_count_sorted = sort_dict(symbol_count)

    # export it:
    export_to_file(symbol_count_sorted, args.output_file_name)


if __name__ == '__main__':
    start_time = time.time()
    if args.script_mode == 'single':
        main_no_threading()
    else:
        main_with_threading()



    print('Затраченное время: ' + format(time.time() - start_time))
