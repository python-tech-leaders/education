import requests
from pathlib import Path



links = ['https://en.wikipedia.org/wiki/Wikipedia',
         'https://en.wikipedia.org/wiki/Wikipedia',
         'https://en.wikipedia.org/wiki/Main_Page',
         'https://en.wikipedia.org/wiki/COVID-19_pandemic',
         'https://ru.wikipedia.org/wiki/Пандемия_COVID-19',
         'https://yi.wikipedia.org/wiki/קאוויד-19_פאנדעמיק',
         'https://tr.wikipedia.org/wiki/COVID-19_pandemisi',
         'https://uk.wikipedia.org/wiki/Пандемія_коронавірусної_хвороби_2019',
         'https://bg.wikipedia.org/wiki/Пандемия_от_коронавирус_(2019_–_2020)',
         'https://be.wikipedia.org/wiki/Пандэмія_COVID-19',
         'https://ro.wikipedia.org/wiki/Pandemia_de_coronaviroză_(COVID-19)',
         ]

def get_data(links):
    data = ''
    for i in links:
        r = requests.get(i)
        data +=  str(r.content)
    return data

def count_sort(data):
    letter_count = {}
    for i in data:
        if i not in letter_count:
            letter_count[i] = 1
        else:
            letter_count[i] += 1
    sort_dict = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    return sort_dict

if __name__ == '__main__':
    data = get_data(links)
    #print(count_sort(data))
