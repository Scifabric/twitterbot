from birdy.twitter import UserClient
import tweepy
from settings import *

client = UserClient(CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

client = tweepy.API(auth)
