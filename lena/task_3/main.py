import threading
import argparse
import json
import time
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


'''No Threading'''
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

def wr_file(sort_dict, file_name):
    p = Path(file_name)
    with p.open("w") as write_file:
        json.dump(sort_dict, write_file, ensure_ascii=False, indent=4)

'''...'''


'''With Threading'''
data = ''
lock = threading.Lock()
def t_load(urls):
    global data
    for url in urls:
        with lock:
            data += get_data(url)


def threading_load(urls,threads_count):
    for i in range(threads_count):
        start = i * len(urls) // threads_count
        stop = (i+1) * len(urls) // threads_count
        thread = threading.Thread(target=t_load, args=(urls[start:stop],))
        thread.start()
        print(thread.name)
        thread.join()
    print('Total letters quantity: {}'.format(len(data)))
    return data
'''...'''

if __name__ == '__main__':
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--output_file_name',
        type=str,
        help='Path to the outputfile in JSON format',
    )
    parser.add_argument(
        '--script_mode',
        type=str,
        choices=('single', 'threaded'),
        help='Script run mode',
    )
    parser.add_argument(
        '--threads_count',
        type=int,
        help='Count of threads',
    )

    args = parser.parse_args()
    if args.script_mode == 'threaded':
        wr_file(count_sort(
            threading_load(links, int(args.threads_count))),
            file_name=args.output_file_name)
    else:
        data = get_data(links)
        dict = count_sort(data)
        wr_file(dict, 'json')
    print('Total time: {}'.format(time.time() - start_time))

