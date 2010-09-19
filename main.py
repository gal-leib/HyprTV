#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import access
from twitter import OAuthApi

twitterapi= None

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        trends = twitterapi.ApiCall("trends","GET")["trends"]
        for trend in trends:
            self.response.out.write("<p>" + trend["name"] + "</p>")
        self.response.out.write("</body></html>")
        #Auto Follow Users

        self.response.out.write("</body></html>")



def main():
#    application = webapp.WSGIApplication([('/', MainHandler)],
#                                         debug=True)
#    util.run_wsgi_app(application)
	global twitterapi
	twitterapi = OAuthApi(access.consumer_key,access.consumer_secret, access.access_token, access.access_secret)


if __name__ == '__main__':
    main()
