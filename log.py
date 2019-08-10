from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp

class LogPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            navbar = ('<p><a href="%s"> Sign in or register</a> </p>' % (users.create_login_url(self.request.path)))
        else:
            navbar = ('<p><a href="%s"> Sign out</a> </p>' % (users.create_logout_url(self.request.path)))

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<p>%s</p>' % (navbar))

logapp = webapp.WSGIApplication([('/do_log',LogPage)],debug = True)

def main():
    run_wsgi_app(logapp)

if __name__ == '__main__':
    main()
