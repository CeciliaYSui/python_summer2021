## MOVE THIS FILE OFF GITHUB REPO BEFORE SYNCING!

## Register an app: https://dev.twitter.com/

#pip install tweepy
import tweepy

## Check the documentation page
## http://docs.tweepy.org/en/v3.2.0/

## Get access to API
## Copy/paste your keys here, move file out of github repo, import keys to public files.
auth = tweepy.OAuthHandler('AK4vWVHiG4bEB5VV2ACFefF7N', 'H79mt6pFgnnlMeDJkW0BBiau95pbN9VW6mR9Za03AAXtpc1EH9')
auth.set_access_token('1354196572435853312-HYmkB3wC6FAtfQSMcB9JmxCuCgC8W4', '370pnT98py7RPN7mlbNnvKzIObWB1xU6y2C1Q4QN1hABZ')    
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

