from tweepy.streaming import StreamListener 
import json
from service.esutil import es
from tweetbot.configure import es_mappings

class TweetyStreamDataListener(StreamListener):
    # on success
    def on_status(self, status):
        hashtags = []
        for hashtag in status.entities['hashtags']:
            hashtags.append(hashtag['text'])

        country = status.place.country if status.place is not None else ""
        country_code = status.place.country_code if status.place is not None else ""

        doc = {
            "screen_name": status.user.screen_name,
            "user_name": status.user.name,
            "location": status.user.location,
            "source_device": status.source,
            "is_retweeted": status.retweeted,
            "retweet_count": status.retweet_count,
            "country": country,
            "country_code": country_code,
            "reply_count": status.reply_count,
            "favorite_count": status.favorite_count,  
            "tweet_text": status.text,
            "created_at": status.created_at,
            "timestamp_ms": status.timestamp_ms,
            "lang": status.lang,
            "hashtags": hashtags
        }

        mappings = es_mappings.get("tweet_index")
        # Creates mapping
        mapping_res = es.indices.create(index="tweets_index", ignore=400,
                                             body=json.dumps(mappings))
        c_res = es.index(index="tweets_index", doc_type="tweet", body=doc)
        return True

    # on failure
    def on_error(self, status):
        print status

