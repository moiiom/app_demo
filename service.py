from base import *


class Service(Base):
    size = 20

    def __init__(self):
        super(Service, self).__init__()

    def get_page_data(self, page_no):
        dsl = {
            "query": {
                "match_all": {}
            },
            "size": self.size,
            "from": self.size * page_no
        }
        result = self.search(dsl)
        data = self.parse(result)
        return data

    def get_detail_by_id(self, newsid):
        dsl = {
            "query": {
                "term": {"_id": str(newsid)}
            }
        }
        result = self.search(dsl)
        data = self.parse(result)
        return data


if __name__ == '__main__':
    s = Service()
    total, messages = s.get_page_data(2)
    print total
    for message in messages:
        print message["url"]
