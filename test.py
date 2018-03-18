from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "CpHdQPGQSJ50QxGWMOSIiiaHX"
consumer_secret = "3LYO2gZcUfn36TNa0zIFYJ7hOrkDnQDZbtTaEgpYHLcVok38Uk"

access_token = "1651820084-7F7vKLbkb18eqpPkxs9v5N6fHvuPNh70pMWR9Sr"
access_token_secret = "74ZhTa8PWFjvNe5RabXP96NPGxQwCXaN3WbAUMteepAYe"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.sample()

    # Other Options
    # stream.filter(track=['basketball'])
    # stream.filter(locations=['-122.75,36.8,-121.75,37.8'])

    # Include every tweet in the world (doesn't work for tweets w/ geotagging off)
    # stream.filter(locations=[-180,-90,180,90])
