# -*- coding: utf-8 -*-
import re
from elasticsearch import Elasticsearch
from myexcepts import *

__all__ = ["Base"]


class Base(object):
    def __init__(self):
        self.index = "weixin"
        self.es = Elasticsearch(['node1:9200', 'node2:9200', 'node3:9200'])

    def search(self, dsl):
        reslut = self.es.search(index=self.index, doc_type=self.index, body=dsl,
                                params={"preference": "_primary_first"})
        if len(reslut['hits']['hits']) == 0:
            raise NoDataException('search es and get no data.')
        return reslut

    def parse(self, result):
        data = list()
        items = result['hits']['hits']
        for i in items:
            record = dict()
            record['id'] = i['_id']
            record['count'] = i['_source'].get('count', '')
            record['postdate'] = i['_source'].get('postdate', '')
            record['like'] = i['_source'].get('like', '')
            content = i['_source'].get('context', '')
            record['context'] = self.digest(content)
            record['title'] = i['_source'].get('title', '')
            record['url'] = i['_source'].get('url', '')
            record['nickname'] = i['_source'].get('nickname', '')
            record['order'] = i['_source'].get('order', '')
            data.append(record)
        d = dict()
        d['status'] = 0
        d['error'] = "ok"
        d['total'] = int(result['hits']['total'])
        d['data'] = data
        return d

    @staticmethod
    def digest(content):
        dr = re.compile(r'<[^>]+>', re.S)
        removed_tag_text = dr.sub('', content)
        replaced_text = removed_tag_text.replace(" ", "").replace("\r", "").replace("\n", "")
        str_len = len(replaced_text)
        if str_len > 300:
            return replaced_text[:300] + "..."
        else:
            return replaced_text
