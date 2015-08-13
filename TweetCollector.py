#Created by Alex Ding
#Python 2.7.1
#Collect tweets via tweepy API
#Last Modified 4/27/2015

###############################################
import sys
import tweepy
import csv
import json
##################################################
consumer_key = "m9NJIKYkgwDBawW9lomDA"
consumer_secret = "AwpRUyN7IiI5wpvw1RjyiAyWbSXYF0IoCqnBFV7uys"
access_token = "150905422-AIsKJBBmXaaD14cjllds1evmntaNBeKov16ZdOvl"
access_secret = "Z00WDDKMS9jkApSoUu09iJRiF3HAxnxy9NyQdUOxKXFtb"




class StdOutListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
#     def on_data(self, data):
#         decoded = json.loads(data)
#         print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
#         print ''
#         return True
    def on_status(self, status):
        temp= status.coordinates
        if temp!=None:
            print temp['coordinates']
        
        
    def on_error(self, status):
        
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    stream = tweepy.Stream(auth, l)
    stream.filter(locations=[-180,-90,180,90], track=['basketball'])