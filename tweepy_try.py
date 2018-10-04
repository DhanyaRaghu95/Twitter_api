import tweepy, json
# Load in OAuth Tokens

fp = open("tweepy_tweets.txt","w")

consumer_key = "efL1w6Qg9KLMlrEZ0lI48lVBQ"
consumer_secret = "kcf0oPAoSUzegPXrna2hDWjDipMqJDxbvkJT7zl6aYdTVuNbkS"
access_token = "1042841244114677760-s6Mk65Nw94ZY29bA35FhKkE8j4B0wg"  #access
access_token_secret = "KaUAg63kvqcfHXfftvLIxDxtKyYvU2zwWfL7R4iwUjWSh"

auth_ = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_)

query = 'Trump'
max_tweets = 100
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, ).items(max_tweets)]
for each in searched_tweets:
    fp.write(str(each))

print(searched_tweets[0])
fp.close()
