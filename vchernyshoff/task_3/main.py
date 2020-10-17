import time
import requests
from langdetect import detect
from pathlib import Path
import threading
import argparse

parser = argparse.ArgumentParser(description='Incredible parser wiki. It shows count of all symbols from asked wiki http(s) pages.')
parser.add_help
all_symbols = ''
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


def get_symbols_from_link(link: str) -> str:
    """get html from link"""
    return requests.get(link).text


def threading_get_symbols_from_link(link: str) -> None:
    """get html from link"""
    global all_symbols
    all_symbols = requests.get(link).text


def get_symbol_set(all_symbols: str) -> set:
    symbol_set = set()

    for symbol in all_symbols:
        symbol_set.add(symbol)
    return symbol_set


def sort_dict(symbol_count: dict) -> str:
    """sort dict by values
    :return: sorted dict"""
    symbol_count_sorted = ''
    for key, val in sorted(symbol_count.items(), key=lambda x: x[1]):
        try:
            if detect(key) == 'fa' or detect(val) == 'ur' or detect(val) == 'he' or detect(val) == 'ar':    # hebrew
                # and other langs works from right to left. We should swap it: "ޑ": 1"
                # perhaps, it would be the best way, use unicode or ASCII codes
                symbol_count_sorted += f'{val} :"{key}"'
                symbol_count_sorted += '\n'
                continue
        except:
            pass
        symbol_count_sorted += f'"{key}": {val}\n'

    return symbol_count_sorted


def main() -> None:
    # # 1) Download all http text with no threading
    # all_symbols = ''
    # for link in links:
    #     all_symbols += get_symbols_from_link(link)

    # 1.1) Download all http text with threading
    global all_symbols
    for link in links:
        thread = threading.Thread(target=threading_get_symbols_from_link, args=(link, ))
        thread.start()
        while threading.active_count() > 1:
            time.sleep(0.05)
            pass
    # 2) Let's create set with symbols which persist in the text and create dict:
    symbol_count = {}
    symbol_set = get_symbol_set(all_symbols)
    for symbol in symbol_set:
        symbol_count[symbol] = 0

    # 3) Now let's count every symbol
    for symbol in all_symbols:
        symbol_count[symbol] += 1

    # 4) Sort dict by values and convert to str:
    symbol_count_sorted = sort_dict(symbol_count)

    # 5) export dit to file symbol_count.txt
    p = Path('symbol_count.txt')
    p.write_text(symbol_count_sorted)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Затраченное время: ' + format(time.time() - start_time))


    # a = detect('ޑ')
    # print(a)


