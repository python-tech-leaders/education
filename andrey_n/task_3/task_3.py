import argparse
import pathlib
import queue
import time
import threading
from collections import Counter


import requests

#  START settings
TARGET = ("https://en.wikipedia.org/wiki/Wikipedia",
          "https://en.wikipedia.org/wiki/Main_Page",
          "https://en.wikipedia.org/wiki/COVID-19_pandemic",
          "https://ru.wikipedia.org/wiki/Пандемия_COVID-19",
          "https://yi.wikipedia.org/wiki/קאוויד-19_פאנדעמיק",
          "https://tr.wikipedia.org/wiki/COVID-19_pandemisi",
          "https://uk.wikipedia.org/wiki/Пандемія_коронавірусної_хвороби_2019",
          "https://bg.wikipedia.org/wiki/Пандемия_от_коронавирус_(2019_–_2020)",
          "https://be.wikipedia.org/wiki/Пандэмія_COVID-19",
          "https://ro.wikipedia.org/wiki/Pandemia_de_coronaviroză_(COVID-19)",)


#  END settings


#  START Parsing text from site
def parse(url: str) -> str:
    """
    Parsing content from url
    :param url - url address of website
    :return: data - all content from website
    """

    data = ""
    try:
        response = requests.request(url=url, method="GET")
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


#  END


#  START single
def single_parsing(urls: tuple) -> str:
    """
    Parser without threading
    :param urls: tuple of urls
    :returns: string of data
    """

    res = ""
    for url in urls:
        res += parse(url)

    return res


#  END


#  START threads
def thread_data(qu: queue, urls: tuple) -> None:
    """
    for one thread target func
    :param qu: queue for getting data
    :param urls: tuple of urls
    """

    for url in urls:
        qu.put(parse(url))


def thread_parse(urls: tuple, threads: int) -> str:
    """
    Running threads target func
    :param urls: tuple of urls
    :param threads: queue for getting data
    :returns: string of data
    """

    q = queue.Queue()
    for i in range(threads):
        start = i * len(urls) // threads
        end = (i + 1) * len(urls) // threads
        thread_i = threading.Thread(target=thread_data, args=(q, urls[start:end]))
        thread_i.start()
        print(thread_i.name)
        thread_i.join()
    res = q.get()

    return res


#  END


#  START Result Output
def result(data: str) -> list:
    """
    Convert result and sort
    :param data: all data from sites
    :returns: list of len and data
    """

    cnt = sorted(dict(Counter(data)).items(), key=lambda item: item[1], reverse=True)
    print("Length of data:", len(data))
    return cnt
#  END


#  START config(write to file)
def log_to_file(data: list, file_name: pathlib.Path) -> None:
    """
    Write to file using pathlib
    :param file_name: name of target file
    :param data: data for writting in file
    """

    with file_name.open("w", encoding="utf8") as file:
        for res in data:
            print(res, file=file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Working with URLS")
    parser.add_argument(
        "--mode",
        default="single",
        choices=("single", "threading"),
        help="Mode for script (Single or threading)",
    )
    parser.add_argument(
        "--file_name",
        default=pathlib.Path("res.txt"),
        type=pathlib.Path,
        help="Write result to .txt in folder",
    )
    parser.add_argument(
        "--threads",
        default=3,
        type=int,
        help="How many threads you need? Write a number.",
    )

    start_time = time.time()
    args = parser.parse_args()
    if args.mode == "single":
        log_to_file(data=result(single_parsing(TARGET)),
                    file_name=args.file_name)
    elif args.mode == "threading":
        log_to_file(data=result(thread_parse(TARGET, abs(args.threads))),
                    file_name=args.file_name
                    )
    print(f"Total time: {time.time() - start_time}")
