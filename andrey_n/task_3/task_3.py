import time
import requests
from collections import Counter
import pathlib
import argparse


TARGET = ["https://en.wikipedia.org/wiki/Wikipedia",
              "https://en.wikipedia.org/wiki/Main_Page",
              "https://en.wikipedia.org/wiki/COVID-19_pandemic",
              "https://ru.wikipedia.org/wiki/Пандемия_COVID-19",
              "https://yi.wikipedia.org/wiki/קאוויד-19_פאנדעמיק",
              "https://tr.wikipedia.org/wiki/COVID-19_pandemisi",
              "https://uk.wikipedia.org/wiki/Пандемія_коронавірусної_хвороби_2019",
              "https://bg.wikipedia.org/wiki/Пандемия_от_коронавирус_(2019_–_2020)",
              "https://be.wikipedia.org/wiki/Пандэмія_COVID-19",
              "https://ro.wikipedia.org/wiki/Pandemia_de_coronaviroză_(COVID-19)",]


#  Parsing text from site
def parser(url: str) -> str:
    """
    Parsing content from url
    :param url - url address of website
    :return: data - all content from website
    """
    data = ''
    try:
        response = requests.request(url=url, method='POST')
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


#  Parsing without threading
def single_parsing(urls: list):
    """
    Parser without threading
    :param urls:
    :returns: Count of symbols
              Time of parsing
              Sorted list of all chars with counts
    """

    start_time = time.time()
    result = ''
    for url in urls:
        result += parser(url)
    len_of_text = len(result)
    single_time = time.time() - start_time
    cnt = sorted(dict(Counter(result)).items(), key=lambda item: item[1], reverse=True)
    print(f"len: {len_of_text}\n"
          f"time: {single_time}\n"
          f"{cnt}")
    return [len_of_text, single_time, cnt]


#  Write to file
def log_to_file(data: list, file_name: str):
    """
    Write to file using pathlib
    :param file_name:
    :param data:
    :return:
    """

    path = pathlib.Path(file_name)


single_parsing(TARGET)

