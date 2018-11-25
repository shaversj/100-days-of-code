import tweepy
import config

auth = tweepy.auth.OAuthHandler(config.consumer_token, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
