import time
import requests
import threading
import pathlib
import argparse
import queue
from collections import Counter


#  START settings
TARGET = ["https://en.wikipedia.org/wiki/Wikipedia",
              "https://en.wikipedia.org/wiki/Main_Page",
              "https://en.wikipedia.org/wiki/COVID-19_pandemic",
              "https://ru.wikipedia.org/wiki/Пандемия_COVID-19",
              "https://yi.wikipedia.org/wiki/קאוויד-19_פאנדעמיק",
              "https://tr.wikipedia.org/wiki/COVID-19_pandemisi",
              "https://uk.wikipedia.org/wiki/Пандемія_коронавірусної_хвороби_2019",
              "https://bg.wikipedia.org/wiki/Пандемия_от_коронавирус_(2019_–_2020)",
              "https://be.wikipedia.org/wiki/Пандэмія_COVID-19",
              "https://ro.wikipedia.org/wiki/Pandemia_de_coronaviroză_(COVID-19)", ]

parser = argparse.ArgumentParser(description='Working with URLS')
parser.add_argument(
    '--mode',
    default='single',
    choices=('single', 'threading'),
    help='Mode for script (Single or threading)',
)
parser.add_argument(
    '--file_name',
    default=pathlib.Path('res.txt'),
    help='Write result to .txt in folder',
)
parser.add_argument(
    '--threads',
    default=3,
    help='How many threads you need? Write a number.',
)
#  END settings


#  START Parsing text from site
def parse(url: str) -> str:
    """
    Parsing content from url
    :param url - url address of website
    :return: data - all content from website
    """
    data = ''
    try:
        response = requests.request(url=url, method='GET')
        response.raise_for_status()
        data = str(response.content)
    except requests.exceptions.HTTPError as err_h:
        print("Http Error:", err_h)
    except requests.exceptions.ConnectionError as err_c:
        print("Error Connecting:", err_c)
    except requests.exceptions.Timeout as err_t:
        print("Timeout Error:", err_t)
    except requests.exceptions.RequestException as err:
        print("Something Else:", err)

    return data


#  single
def single_parsing(urls: list) -> list:
    """
    Parser without threading
    :param urls:
    :returns: Count of symbols
              Time of parsing
              Sorted list of all chars with counts
    """

    result = ''
    for url in urls:
        result += parse(url)
    len_of_text = len(result)
    cnt = sorted(dict(Counter(result)).items(), key=lambda item: item[1], reverse=True)

    return [len_of_text, cnt]


# threadings

def thread_data(qu, urls):
    for url in urls:
        qu.put(parse(url))


def thread_parse(urls: list, threads: int) -> list:
    q = queue.Queue()
    for i in range(threads):
        start = i * len(urls) // threads
        end = (i+1) * len(urls) // threads
        thread_i = threading.Thread(target=thread_data, args=(q, urls[start:end]))
        thread_i.start()
        print(thread_i.name)
        thread_i.join()
    res = q.get()
    cnt = sorted(dict(Counter(res)).items(), key=lambda item: item[1], reverse=True)
    print(f"All chars: {len(res)}")

    return [len(res), cnt]
#  END


#  START config(write to file)
def log_to_file(data: list, full_time: time, file_name: str) -> None:
    """
    Write to file using pathlib
    :param full_time:
    :param file_name:
    :param data:
    :return:
    """

    path = pathlib.Path(file_name)
    with path.open('w', encoding='utf8') as file:
        print(f"All chars: {data[0]}\n Time for parsing: {full_time}", file=file)
        for res in data[1]:
            print(res, file=file)


#  run scripts
def main():
    """
    run script
    :return:
    """
    start_time = time.time()
    args = parser.parse_args()
    if args.mode == 'single':
        log_to_file(data=single_parsing(TARGET),
                    full_time=time.time() - start_time,
                    file_name=args.file_name)
    elif args.mode == 'threading':
        log_to_file(data=thread_parse(TARGET, int(args.threads)),
                    full_time=time.time() - start_time,
                    file_name=args.file_name
                    )
# END


if __name__ == "__main__":
    main()


