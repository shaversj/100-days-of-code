import tweepy_api_config
import csv


class UserTweets(object):

    def __init__(self, handle):
        self.handle = handle
        #self.max_id = max_id
        self.tweets = tweepy_api_config.api.user_timeline(screen_name=handle, count=10,
                                                          include_rts=False, tweet_mode='extended')

    def __len__(self):

        return len(self.tweets)

    def __getitem__(self, position):
        tweet_list = []
        tweet_list.clear()

        for data in self.tweets:
            tweet_id = str(data['id'])
            tweet_date = data['created_at']
            full_text = data['full_text']

            tweet = [tweet_id, tweet_date, full_text]
            tweet_list.append(tweet)

        return tweet_list[position]

    def wrtite_csv(self):
        """Write tweets to CSV file"""
        with open(self.handle, mode='w') as tweet_file:
            tweet_writer = csv.writer(tweet_file)

            for data in self.tweets:
                tweet_id = str(data['id'])
                tweet_date = data['created_at']
                full_text = data['full_text']
                tweet_writer.writerow([tweet_id, tweet_date, full_text])


if __name__ == "__main__":

    trump = UserTweets('realDonaldTrump')
    print(len(trump.tweets))
    # print(len(trump))
    print(trump[1:4])
    trump.wrtite_csv()
