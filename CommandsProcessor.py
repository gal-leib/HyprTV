import re
from  models.reminder import *
from  models.tv_show import *
import access
from libs.twitter import OAuthApi

#Todo: Clean the print debug code

cmd_pattern = "^([A-Za-z_]*) ([A-Za-z0-9!@#$%^&*: =?><';-]*)"
twitterapi = None

def process_DM(dm):
    message = dm["text"]
    user = dm["sender"]["screen_name"]
    print(dm["text"])
    match = re.match(cmd_pattern, message)
    if match:
        print("Match")
        cmd = match.group(1)
        if hasattr(_Commands_Processor, cmd):
            print(cmd + ' ' + match.group(2))
            try:
                getattr(_Commands_Processor, cmd)(user, match.group(2))
            except Exception, e:
            #  CLEAN THIS MOTHERFUCKER UGLY CODE
                print(e)
                print('FML')
                raise Exception

def _check_pattern(pattern):
    def outsider(func):
        def insider(*args, **kwargs):
            match = re.match(pattern, args[1])
            if match:
                kwargs.update(match.groupdict())
                return func(*args, **kwargs)
        return insider
    return outsider

class _Commands_Processor():
    @staticmethod
    @_check_pattern("'(?P<tv_show_name>[A-Za-z0-9!@#$%^&* =?><-]*)'")
    def follow(user, params, **kwargs):
        ''' follow 'Fringe' '''
        try:
            reminder = Reminder()
            reminder.user = user
            reminder.tv_show = get_tv_show_by_name(kwargs['tv_show_name'])
            reminder.put()
            twitterapi.SendDM(user, "You are now following the TV show: " + kwargs['tv_show_name'])
        except:
            twitterapi.SendDM(user,
                              "Couldn't add the reminder. Maybe " + kwargs['tv_show_name'] + " isn't in our database yet."
                              )
            print("Couldn't add the reminder. Maybe the show isn't in our database yet")

    @staticmethod
    @_check_pattern("'(?P<tv_show_name>[A-Za-z0-9!@#$%^&* =?><-]*)'")
    def unfollow(user, params, **kwargs):
        '''unfollow 'Fringe' '''
        try:
            reminder = get_single_reminder(user, kwargs['tv_show_name'])
            reminder.delete()
            twitterapi.SendDM(user, "You are now NOT following the TV show: " + kwargs['tv_show_name'])
        except:
            twitterapi.SendDM(user, "Couldn't delete the reminder. Maybe it's nonexistent or you got the name wrong?")
            print "Couldn't delete the reminder. Maybe it's nonexistent or you got the name wrong?"





        #@staticmethod
        #def add_show(user, params):
        #'''add_show 'Fringe' 3 17:21'''
        #pass

def main():
    global twitterapi
    twitterapi = OAuthApi(access.consumer_key, access.consumer_secret, access.access_token, access.access_secret)
    dms = twitterapi.GetDirectMessages()
    if dms:
        for dm in dms:
            print("Processing DM ")
            try:
                process_DM(dm)
            except:
                print 'FML'
            else:
                print("DM processed\n")
                twitterapi.DeleteDM(dm["id"])

if __name__ == '__main__':
    main()
  