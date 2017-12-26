# encoding: utf-8

import webapp2
import random
import time
import os


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        msg = u""
        # msg += u"HTTP_HOST: {0}\n".format(os.environ.get("HTTP_HOST", ""))
        msg += u"INSTANCE_ID: {0}".format(os.environ.get("INSTANCE_ID", ""))
        self.response.write(msg)


class ErrorPage(webapp2.RequestHandler):
    def get(self):
        tmp = ["hello"]
        tmp[1] # Error


class SlowPage(webapp2.RequestHandler):
    def get(self):
        t = random.random() * 3
        time.sleep(t)

        msg = u""
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(u"Wait: {} mins...".format(t))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/error', ErrorPage),
    ('/slow', SlowPage),
], debug=True)
