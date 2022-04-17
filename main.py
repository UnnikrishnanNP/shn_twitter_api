import tweepy
import configparser

# config used for geting the keys
config = configparser.RawConfigParser()
config.read('config.ini')

# saving those keys in respective variables
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# api calling
api = tweepy.API(auth, wait_on_rate_limit=True)

# getting user details
name = input("Enter username with @ : ")
user = tweepy.Cursor(api.search_users, q=name).items(1)
for i in user:
    print(f"Name : {i.name}")
    print(f"Followers: {i.followers_count}")
    print(f"Following : {i.friends_count}")
    print(f"Image URL : {i.profile_image_url}")
    print(f"Place : {i.location}")
    if i.verified:
        verified = "Yes"
    else:
        verified = "No"
    print(f"Verfied : {verified}")

# tweets count
tweets_list = list(tweepy.Cursor(api.user_timeline, screen_name=name).items())
count = len(tweets_list)
print(f"No. of tweets: {count}")

# last 10 tweets
tweets = tweepy.Cursor(api.user_timeline, screen_name=name).items(10)
print(f"{name}'s latest 10 tweets")
print("---------------------------")
for tweet in tweets:
    print(f"{tweet.text}\n")
