# encoding: utf-8

import webapp2
import random
import time
import os


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        msg = u""
        # msg += u"Hostname: {0}".format(os.environ.get("HTTP_HOST", ""))
        msg += u"Hostname: {0}".format(os.environ.get("INSTANCE_ID", ""))
        self.response.write(msg)


class ErrorPage(webapp2.RequestHandler):
    def get(self):
        tmp = ["hello"]
        return tmp[1]


class SlowPage(webapp2.RequestHandler):
    def get(self):
        time.sleep(random.random() * 3)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Too Slow...')


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/error', ErrorPage),
    ('/slow', SlowPage),
], debug=True)
