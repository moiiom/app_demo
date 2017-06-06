import tornado.escape
import tornado.ioloop
import tornado.web
import os.path
from tornado.options import define, options, parse_command_line

from service import *

define("port", default=8888, help="run on the given port", type=int)

serv = Service()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class ListHandler(tornado.web.RequestHandler):
    def get(self):
        page_no = int(self.get_argument("page", 0))
        data = serv.get_page_data(page_no)
        self.write(data)


class DetailHandler(tornado.web.RequestHandler):
    def post(self):
        newsid = self.get_argument("id") or ""
        data = serv.get_detail_by_id(newsid)
        self.write(data)


def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/list", ListHandler),
            (r"/detail", DetailHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
