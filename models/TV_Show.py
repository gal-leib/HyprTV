from google.appengine.ext import db
from datetime import datetime

class TV_Show(db.Model):
    name = db.StringProperty('Show Name')
    day = db.IntegerProperty('Air Day', choices=set([1,2,3,4,5,6,7]))
    time = db.TimeProperty('Air Time')
    status = db.StringProperty('Status', choices=set(["Airing", "Not Airing"]))

    @classmethod
    def new(cls,name, day, time, status,tz='US/Eastern'):
        tv_show = cls(name=name, day=day, status=status)
        #Todo: Implement time setting.


    def minutes_till_starts(self):
        now = datetime.now().hour * 60 + datetime.now().minute
        showtime = self.time.hour * 60 + self.time.minute
        return showtime - now

def get_tv_show_by_name(name):
    ''' Get's a TV Show by it's name '''
    tv_query = TV_Show.all()
    tv_query.filter('name =', name)
    results =  tv_query.fetch(1)
    if not results:
        raise Exception
    return results[0]


#def diff_time_in_min(t1, t2):
#    t1_min = t1.hour * 60 + t1.minute
#    t2_min = t2.hour * 60 + t2.minute
#    return abs(t1_min - t2_min)
##return t1_min - t2_min