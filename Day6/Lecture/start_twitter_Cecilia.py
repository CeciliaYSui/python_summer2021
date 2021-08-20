## MOVE THIS FILE OFF GITHUB REPO BEFORE SYNCING!

## Register an app: https://dev.twitter.com/

#pip install tweepy
import tweepy

## Check the documentation page
## http://docs.tweepy.org/en/v3.2.0/

## Get access to API
## Copy/paste your keys here, move file out of github repo, import keys to public files.
auth = tweepy.OAuthHandler('consumer key', 'consumer')
auth.set_access_token('access token', '')    
client = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


"""

# Testing authentication worked 
import importlib
import tweepy
from pprint import pprint
# http://docs.tweepy.org/en/v3.8.0/api.html

twitter = importlib.import_module('start_twitter_Cecilia')
api = twitter.client

# See rate limit
limit = api.rate_limit_status()
pprint(limit)
# print(limit.keys()) ##look at dictionary's keys
# prepare for dictionaries all the way down

print()
joe = api.get_user('@JoeBiden')
print(joe)
"""

