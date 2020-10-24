import json

import olxscrapper

if __name__ == '__main__':
    res = olxscrapper.get_data()
    print(res)
    with open("data_file.json", "w", encoding='utf-8') as write_file:
        json.dump([dict(i) for i in res], write_file, ensure_ascii=False)
