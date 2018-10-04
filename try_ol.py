from datetime import datetime
import json
import codecs
from twython import TwythonStreamer, Twython

# Load in OAuth Tokens

tweets                          =   []
MAX_ATTEMPTS                    =   10
COUNT_OF_TWEETS_TO_BE_FETCHED   =   500 

dt = datetime.now()
filename = "data/example-search-proper-%s.txt" % (dt.strftime("%Y-%m-%d"),)
fp = codecs.open(filename, 'w', encoding='utf-8',errors='ignore')

twitter = Twython(app_key, app_sec, user_key, user_sec)

for i in range(0,MAX_ATTEMPTS):

    if(COUNT_OF_TWEETS_TO_BE_FETCHED < len(tweets)):
        break # we got 500 tweets... !!

    #----------------------------------------------------------------#
    # STEP 1: Query Twitter
    # STEP 2: Save the returned tweets
    # STEP 3: Get the next max_id
    #----------------------------------------------------------------#

    # STEP 1: Query Twitter
    print(i)
    if(0 == i):
        print("if loop")
        # Query twitter for data. 
        results    = twitter.search(q="",count='100', result_type="recent")
    else:
        print("entering the else part of the loop")
        # After the first call we should have since_id from result of previous call. Pass it in query.
        results    = twitter.search(q="Trump",include_entities='true', count='100', since_id=next_since_id, result_type="recent")

    # STEP 2: Save the returned tweets
    for result in results['statuses']:
        fp.write(json.dumps(result))
        fp.write("\n")

    # STEP 3: Get the next since_id
    try:
        # Parse the data returned to get max_id to be passed in consequent call.
        next_results_url_params = results['search_metadata']['next_results']
        print(next_results_url_params)
        next_since_id = next_results_url_params.split('max_id=')[1].split('&')[0]
    except:
        # No more next pages
        break
