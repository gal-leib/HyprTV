= Description = 

This is a project to combine 

python-twitter (http://code.google.com/p/python-twitter/)
oauth-python-twitter (http://code.google.com/p/oauth-python-twitter/) 

to provide an easy to use python twitter interface that is oAuth authenticated. 

= Requirements =

Tested with python-2.6
simplejson
oauth2

both simplejson and oauth2 are available through easy_install

= Example =

# replace the parameters with your oAuth authentication data
twitter = OAuthApi(consumer_key, consumer_secret, token, token_secret)

#returns a dict formatted from the JSON data returned
apiData = twitter.ApiCall("account/rate_limit_status", "GET")

= Contact =

Please use the Issues section of the project homepage at:

http://code.google.com/p/oauth-python-twitter2/

Please note that I am working on making wrappers for basic calls
like getting followers and sending status updates.
