import os
import sys
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(['node1:9200', 'node2:9200', 'node3:9200'])
index_name = "weixin"
files_path = "../data"


def get_all_files():
    file_name = []
    for parent, dirnames, filenames in os.walk(files_path):
        for filename in filenames:
            # print "filename is:" + filename
            file_name.append(os.path.join(parent, filename))
    return file_name


def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


def load_data():
    data = []
    file_names = get_all_files()
    file_count = len(file_names)

    for i in range(file_count):
        name = file_names[i]
        with open(name, 'r') as f:
            url = f.readline().strip('\n')
            title = f.readline().strip('\n')
            postdate = f.readline().strip('\n') or ""
            order = f.readline().strip('\n') or ""
            count = f.readline().strip('\n') or "0"
            like = f.readline().strip('\n') or "0"
            nickname = f.readline().strip('\n') or ""
            context = f.read()

            action = {
                "_index": index_name,
                "_type": index_name,
                "_id": md5(url),
                "_source": {
                    "url": url,
                    "title": title,
                    "postdate": postdate,
                    "order": order,
                    "count": count,
                    "like": like,
                    "nickname": nickname,
                    "context": context,
                    "timestamp": datetime.now()}
            }
            data.append(action)
        if i % 30 == 0 or i == file_count - 1:
            print("loading to elasticsearch index...")
            helpers.bulk(es, data)


if __name__ == '__main__':

    is_exists = es.indices.exists(index_name)
    if not is_exists:
        print("index:{0} is not exists.script exit!")
        sys.exit(0)

    load_data()
