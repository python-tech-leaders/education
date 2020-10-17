import requests
from langdetect import detect




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

def get_symbol_set(all_symbols: str) -> set:
    symbol_set = set()

    for symbol in all_symbols:
        symbol_set.add(symbol)
    return symbol_set



def main() -> None:
    # 1) Download all http text
    all_symbols = ''
    for link in links:
        all_symbols += get_symbols_from_link(link)

    # 2) Let's create set with symbols which persist in the text and create dict:
    symbol_count = {}
    symbol_set = get_symbol_set(all_symbols)
    for symbol in symbol_set:
        symbol_count[symbol] = 0

    # 3) Now let's count all_symbols
    for symbol in all_symbols:
        symbol_count[symbol] += 1

    # 4) Sort dict by values:

    # for key, val in sorted(symbol_count.items(), key=lambda x: x[1]):
    for key, val in sorted(symbol_count.items(), key=lambda x: x[1]):
        try:
            if detect(key) == 'fa' or detect(val) == 'ur' or detect(val) == 'he':    # hebrew and other langs works from right to left. We should swap it: "ޑ": 1"
                print(f'{val}: "{key}"')
                continue
        except:
            pass

        print(f'"{key}": {val}')





if __name__ == '__main__':
    main()


