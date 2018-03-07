from tweepy import Stream
from service.twitter.listener.tweety_listener import TweetyStreamDataListener
from configure import twitter_config
import time

class Tweety(object):
    def __init__(self, listener=TweetyStreamDataListener()):
        self.listener = listener
        self.__auth__ = None

    def __authenticate__(self):
        from tweepy import OAuthHandler
        if self.__auth__ is None:
            self.__auth__ = OAuthHandler(twitter_config['consumer_key'], twitter_config['consumer_secret'])
            self.__auth__.set_access_token(twitter_config['access_token'], twitter_config['access_token_secret'])
        return self.__auth__ is not None

    def __streamer__(self):
        is_authenticated = self.__authenticate__()
        if is_authenticated:
            return Stream(self.__auth__, self.listener)
        return None

    def filter(self, keywords=None, runtime = None , async=True):
        '''How long do you want to stream tweets (in seconds)'''
        print runtime
        if(runtime == None):
            runtime = 30  #default

        streamer = self.__streamer__()
        try:
            print "[STREAM] Started stream using keywords", keywords
            streamer.filter(track=keywords, async=async)
            time.sleep(runtime) #halts the control for runtime seconds
            streamer.disconnect() #disconnect the stream and stop streaming
            print ("done....")
            
        except Exception as ex:
            print "[STREAM] Stream stopped! Reconnecting to twitter stream, keywords", keywords
            print ex.message, ex.args
            self.filter(keywords=keywords, async=async)
            time.sleep(runtime) #halts the control for runtime seconds
            streamer.disconnect() #disconnect the stream and stop streaming
            print ("done....")