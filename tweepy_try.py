import tweepy, json
# Load in OAuth Tokens

fp = open("tweepy_tweets.txt","w")



auth_ = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_)

query = 'python'
max_tweets = 100
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, ).items(max_tweets)]
for each in searched_tweets:
    fp.write(str(each))

print(searched_tweets[0])
fp.close()
