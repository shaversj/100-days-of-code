import tweepy
import config
import json
import csv

auth = tweepy.auth.OAuthHandler(config.consumer_token, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
#api = tweepy.API(auth)

userID = "realDonaldTrump"
tweets = api.user_timeline(screen_name=userID, count=3,
                           include_rts=False, tweet_mode='extended')

tweet_data = []


""" for data in tweets:
    tweet = {'id_str': data.id, 'created_at': data.created_at,
             'full_text': data.full_text}
    tweet_data.append(tweet) """


# print(tweet_data)

#json_str = json.dumps(tweet_data, indent=4, sort_keys=True, default=str)

# print(tweet_data[0]['id_str'].values)

#tweet_json = json.dumps(tweets, indent=4, sort_keys=True, default=str)

#tweet_json = json.dumps(tweets)

tweet_list = []

for data in tweets:
    tweet_id = str(data['id'])
    tweet_date = data['created_at']
    full_text = data['full_text']

    tweet = [tweet_id, tweet_date, full_text]
    tweet_list.append(tweet)


print(tweet_list[0])
# print(tweet_json[2])
