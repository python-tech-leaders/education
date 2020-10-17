import threading

import requests
from requests import HTTPError


def _get_data(url):
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


def get_data_by_single_thread(urls):
    responses = []
    for url in urls:
        responses.append(_get_data(url))
    return responses


_result = []
_lock = threading.Lock()


def _kernel_thread(*args):
    urls = list(args)
    global _result
    with _lock:
        _result += get_data_by_single_thread(urls)


def get_data_by_more_thread(urls, count_thread=4):
    threads = []
    for i in range(count_thread):
        start_index = i * (len(urls) % count_thread)
        finish_index = 0
        if (i + 1) * (len(urls) % count_thread) >= len(urls):
            finish_index = len(urls) - 1
        else:
            finish_index = (i + 1) * (len(urls) % count_thread)
        threads.append(threading.Thread(target=_kernel_thread, args=(list(urls[start_index:finish_index]))))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return _result
