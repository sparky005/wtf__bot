import tweepy
import consumer
import random

def post_tweet(tweet, api):
    """Post tweet"""
    api.update_status(tweet)

def get_api():
    """Get authentication information and create API"""
    auth = tweepy.OAuthHandler(consumer.CONSUMER_KEY, consumer.CONSUMER_SECRET)
    auth.set_access_token(consumer.ACCESS_KEY, consumer.ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def main():
    api = get_api() # get twitter api
    tweet = ['WTF', 'WTF?!', 'WTF!', 'WTF?', 'wtf!']
    i = random.randint(0,7)
    print(i)
    if i < 5:
        post_tweet(tweet[i], api)

# run
if __name__ == "__main__":
    main()
