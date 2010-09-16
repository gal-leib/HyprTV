from google.appengine.ext import db

class AppUser(db.Model):
    twitter_name = db.StringProperty('Twitter User Name')

  