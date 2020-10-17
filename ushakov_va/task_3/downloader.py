import threading

import requests
from requests import HTTPError


def _get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.text


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
        threads.append(threading.Thread(target=_kernel_thread, args=(list(urls[i * (len(urls) % count_thread): len(
            urls) - 1 if (i + 1) * (len(urls) % count_thread) >= len(urls) else (i + 1) * (
                    len(urls) % count_thread)]))))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return _result
