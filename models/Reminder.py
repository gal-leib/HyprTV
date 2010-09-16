from google.appengine.ext import db
from models.TV_Show import TV_Show

class Reminder(db.Model):
	#ToDo: Choose how to work with users.
	user = db.IntegerProperty('Twitter User') #Maybe use this without a User data enitity?
	#user = db.StringProperty('Twitter User')
	# user = db.ReferenceProperty(models.User)
	tv_show = db.ReferenceProperty(TV_Show)
	#ToDo: Choose how to implement time before the show airs. for now 30 min before

	@staticmethod
	def get_single_reminder(user, tv_show):
		'''Get's a reminder by the user and the name of the TV Show'''
		reminder_query = Reminder.all()
		reminder_query.filter('user =', user).filter('tv_show.name = ', tv_show)
		results = reminder_query.fetch(1)
		if not results:
			raise Exception('No Reminder!')
		return results[0]