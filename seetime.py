from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import datetime

class MainPage(webapp.RequestHandler):
    def get(self):
        time = datetime.datetime.now()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<p> The time iss: %s </p>' % str(time))

application = webapp.WSGIApplication([('/see_time',MainPage)], debug = True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()

