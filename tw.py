import tweepy
import time

# Tweepy and time libraries are imported.
# tweepy: Used to interact with the Twitter API.
# time: Used for handling delays (like rate limits).

# These commented-out lines show an alternative way to authenticate with consumer keys and access tokens.
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# Replace the placeholders with your actual keys and tokens to authenticate your bot with the Twitter API.
auth = tweepy.OAuthHandler('YEtyk4MJMQEwOu6RDThzcczAN', 'O8vqhyncDn0C3DbFB8SSnEedk8mFMvVaQTDbpSNh2FawL3wwvD')
auth.set_access_token('1813666908388093954-AzO8TYFzwoGXap4ypvFQUUcxGHdXhZ', 'CtWU3aNyWuMHiMdIuyCAwf0HV3srpYKhLg5jIzTLSkkj4')

# Creating an API object to interact with Twitter using the authenticated credentials.
api = tweepy.API(auth)

# This commented-out section shows how to fetch the timeline of a specific user (e.g., 'raisul_islam072') and print tweet content.
# public_tweets = api.user_timeline(user_id='raisul_islam072', tweet_mode='extended')
# for tweet in public_tweets:
#     print(tweet.text)

# This commented-out line fetches details about the authenticated user (the bot itself) and prints the information.
# user = api.me()
# print(user)

# Function to handle Twitter API rate limits.
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()  # This fetches the next item in the cursor (e.g., tweets, followers).
    except tweepy.RateLimitError:  # If rate limit is reached, the bot will pause.
        time.sleep(1000)  # Waits 1000 seconds before trying again.

# Setting the keyword to search for in tweets and the number of tweets to interact with.
search_string = 'python'
numbersOfTweets = 2

# This loop searches for tweets containing the keyword 'python' and interacts with them.
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()  # Likes (favorites) the tweet.
        print("I liked that tweet")  # Print a message to confirm the action.
    except tweepy.TweepError as e:  # Handles any Tweepy-related errors.
        print(e.reason)  # Prints the reason for the error.
    except StopIteration:  # Stops the loop when there are no more tweets to process.
        break

# This commented-out section shows how the bot can follow a specific user if they are among the followers.
# for follower in tweepy.Cursor(api.followers).items():
#     if follower.name == 'Nnesandz_05':  # Replace 'Nnesandz_05' with the target follower's name.
#         follower.follow()  # Follows the user if the condition is met.
#         break  # Stops the loop after following the user.
