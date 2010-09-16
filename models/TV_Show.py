from google.appengine.ext import db

class TV_Show(db.Model):
    name = db.StringProperty('Show Name')
    day = db.IntegerProperty('Air Day', choices=set([1,2,3,4,5,6,7]))
    time = db.TimeProperty('Air Time')
    status = db.StringProperty('Status', choices=set(["Airing", "Hiatus"]))

    @staticmethod
    def get_tv_show_by_name(tv_show):
	tv_query = TV_Show.all()
	tv_query.filter('name =', tv_show)
	results =  tv_query.fetch(1)
	if not results:
		raise Exception
	return results[0]