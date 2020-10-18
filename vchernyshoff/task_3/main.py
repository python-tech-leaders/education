import time
import requests
from pathlib import Path
import threading
import argparse

parser = argparse.ArgumentParser(description='Incredible parser wiki. It shows count of all symbols from asked wiki http(s) pages.')
parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('output-file-name', type=str, help='set name of an output file')
parser.add_argument('script-mode{threaded, single}', type=str, help='Script run mode')
parser.add_argument('threads_count{true, false}', type=str, help='Show count of threads')
args = parser.parse_args()

symbol_count = {}
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
    return requests.get(link).text


def sort_dict(symbol_count: dict) -> str:
    """sort dict by values
    :return: sorted dict"""
    symbol_count_sorted = ''
    for key, val in sorted(symbol_count.items(), key=lambda x: x[1]):
        symbol_count_sorted += f'"{key}": {val}\n'
    return symbol_count_sorted


def export_to_file(text: str) -> None:
    """save text to file symbol_count.txt"""
    p = Path('symbol_count.txt')
    p.write_text(text)



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
    export_to_file(symbol_count_sorted)


# ======================with threading:==========================================
def threading_get_symbols_from_link(link: str) -> None:
    """get html from link"""
    global symbol_count

    text = requests.get(link).text  # get text from wiki
    for symbol in text:
        try:
            symbol_count[symbol] += 1
        except:
            symbol_count[symbol] = 1


def main_with_threadng():
    global symbol_count
    # 1) Download all http text with threading and create set:
    for link in links:
        thread = threading.Thread(target=threading_get_symbols_from_link, args=(link, ))
        thread.start()

    while threading.active_count() > 1:
        time.sleep(0.01)

    # we have symbol count set. Let's sort it
    symbol_count_sorted = sort_dict(symbol_count)

    # export it:
    export_to_file(symbol_count_sorted)


if __name__ == '__main__':
    start_time = time.time()
    # if threading_switch is True:
    #     main_with_threading()
    # else:
    #     main_no_threading()

    main_no_threading()
    # main_with_threadng()

    print('Затраченное время: ' + format(time.time() - start_time))

