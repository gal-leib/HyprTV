from google.appengine.ext import db
from models.tv_show import TV_Show, get_tv_show_by_name

class Reminder(db.Model):
	user = db.StringProperty("Twitter User's Screen Name")
	tv_show = db.ReferenceProperty(TV_Show)
	#ToDo: Choose how to implement time before the show airs. for now 30 min before

def get_single_reminder(user, tv_show):
	'''Get's a reminder by the user and the name of the TV Show'''
	reminder_query = Reminder.all()
	reminder_query.filter('user =', user).filter('tv_show = ', get_tv_show_by_name(tv_show).key())
	results = reminder_query.fetch(1)
	if not results:
		raise Exception('No Reminder!')
	return results[0]