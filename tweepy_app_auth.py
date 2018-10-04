import tweepy
import codecs, json, time
from datetime import datetime

app_key = ""
app_sec = ""
user_key = ""  #access
user_sec = ""

tweetsPerQry = 100
searchQuery = "python"
maxid=None
max_tries = 1000000000
max_tweets = 45000
count = 0

dt = datetime.now()
filename = "data/example-search-tweepy-2-%s.txt" % (dt.strftime("%Y-%m-%d"),)
fp = codecs.open(filename, 'w', encoding='utf-8',errors='ignore')

auth = tweepy.OAuthHandler(app_key, app_sec)

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

while count <= max_tweets:
    try:
        if(not maxid):
            new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
        else:
            #print("tweet ID since", maxid)
            new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since_id = str(maxid-1))
        count += len(new_tweets)
        for each in new_tweets:
            fp.write(str(each.id))
            fp.write("\n")

        #update the since_id to the max_id of the previous run
        try:
            #print("updating sinceid", new_tweets[0].id)
            maxid = new_tweets[-1].id
        except tweepy.TweepError as e:
            print(e)
            #break
    except tweepy.TweepError as e:
        print(e)
        break

fp.close()
