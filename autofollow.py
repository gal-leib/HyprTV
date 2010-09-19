import access
from twitter import OAuthApi

#ToDo: Choose a method


def old():
	'''Returns 5000 followers and friends at a time and checks them'''
	twitterapi = OAuthApi(access.consumer_key,access.consumer_secret, access.access_token, access.access_secret)
	friends = twitterapi.GetFriendsIDs()
	followers = twitterapi.GetFollowersIDs()
	for f in followers:
		if f not in friends:
			twitterapi.FollowUser(f)

def new():
	'''Returns 100 followers at a time'''
	twitterapi = OAuthApi(access.consumer_key,access.consumer_secret, access.access_token, access.access_secret)
	followers = twitterapi.GetFollowers()
	for follower in followers:
		if not follower["following"]:
			twitterapi.FollowUser(follower["id"])


if __name__ == '__main__':
    old()
