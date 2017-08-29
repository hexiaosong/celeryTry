import tornado
import tornado.ioloop
import time
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
#import tornado.gen

class MainHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(40)

#    @tornado.web.asynchronous
#    @tornado.gen.coroutine
    def get(self):
        print(time.asctime())
        yield self.sleep(6)
        self.write('from server:' + time.asctime())
        self.finish()

    @run_on_executor
    def sleep(self, sec):
        time.sleep(sec)


if __name__ == '__main__':
    app = tornado.web.Application(handlers=[
        ('^/.*', MainHandler)
    ])
    app.listen(10240)
    tornado.ioloop.IOLoop.instance().start()
