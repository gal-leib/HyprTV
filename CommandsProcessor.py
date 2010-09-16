from models.Reminder import Reminder
from models.TV_Show import TV_Show
import re
import access
from twitter import OAuthApi

#Todo: Clean the print debug code

cmd_pattern =  "^([A-Za-z_]*) '([A-Za-z0-9!@#$%^&* =?><-]*)'"
twitterapi = None

def process_DM(dm):
	message = dm["text"]
	user = dm["sender"]["screen_name"]
	print(dm["text"])
	match = re.match(cmd_pattern, message)
	if match:
		print("Match")
		cmd = match.group(1)
		if hasattr(Commands_Processor, cmd):
			print(cmd + ' ' + match.group(2))
			try:
				#tv_show = TV_Show.get_tv_show_by_name(match.group(2))
				getattr(Commands_Processor,cmd)(user, match.group(2))
			except:
				print('FML')

class Commands_Processor():
	@staticmethod
	def add_reminder(user, tv_show):
		try:
			reminder = Reminder()
			reminder.user=user
			reminder.tv_show=TV_Show.get_tv_show_by_name(tv_show)
			reminder.put()
		except:
			twitterapi.SendDM(user, "Couldn't add the reminder. Maybe the show isn't in our database yet.")
			print("Couldn't add the reminder. Maybe the show isn't in our database yet")

	@staticmethod
	def del_reminder(user, tv_show):
		try:
			reminder = Reminder.get_single_reminder(user,tv_show)
			reminder.delete()
		except:
			twitterapi.SendDM(user, "Couldn't delete the reminder. Maybe it's nonexistent or you got the name wrong?")


def main():
	global twitterapi
	twitterapi = OAuthApi(access.consumer_key,access.consumer_secret, access.access_token, access.access_secret)
	dms = twitterapi.GetDirectMessages()
	if dms:
		for dm in dms:
			print("Processing DM \n")
			process_DM(dm)
	        print("DM processed\n")
	        twitterapi.DeleteDM(dm["id"])

if __name__ == '__main__':
	main()
  