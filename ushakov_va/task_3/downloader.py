import threading

import requests
from requests import HTTPError


def _get_data(url):  # method for get full text html page
    data = ""
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return data


def get_data_by_single_thread(urls):  # get texts of pages by single thread
    responses = []
    for url in urls:
        responses.append(_get_data(url))
    return responses


_result = []  # a shared variable for threads
_lock = threading.Lock()  # a lock to control the use of _result by multiple threads


def _kernel_thread(*args):  # kernel of one thread
    urls = list(args)
    global _result
    with _lock:  # control of access to shared resources
        _result += get_data_by_single_thread(urls)


def get_data_by_more_thread(urls, count_thread=4):
    threads = []
    for i in range(count_thread):
        start_index = i * (len(urls) % count_thread)  # counting start index fot this thread
        finish_index = 0
        if (i + 1) * (len(urls) % count_thread) >= len(urls): # counting start index fot this thread
            finish_index = len(urls) - 1
        else:
            finish_index = (i + 1) * (len(urls) % count_thread)

        threads.append(threading.Thread(target=_kernel_thread, args=(list(urls[start_index:finish_index]))))  # getting a part of list for this thread and create thread
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return _result
