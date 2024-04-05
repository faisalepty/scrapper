import tweepy

# Twitter API credentials
API_KEY = 'on3mdncBEbCllvqGyvofJ7Sd0'
API_SECRET_KEY = 'IrANKAQif8HqmU2k9s8byt8cFUMbWYUcLImwpFd3lHKQ0J3llv'
ACCESS_TOKEN = '1489158343927156739-xp6XLz04J3NyNaxzMR9VBB3NaNRc3T'
ACCESS_TOKEN_SECRET = 'mloNH41ztVhDuGDyxfDQGDSo6Z19LpRt7ZnIshf89RgOB'

def authenticate_twitter_api():

    """
    Authenticate with the Twitter API using Tweepy.
    """
    client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)
    return client

def post_tweet(api, tweet_content):
    """
    Post a tweet using the authenticated API.
    """
    try:
        api.create_tweet(text=tweet_content)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Authenticate with the Twitter API
    twitter_api = authenticate_twitter_api()
    # Example tweet content (replace with your desired content)
    tweet_content = "Hello Twitter! This is a test tweet from my Python automation tool."
    # Post the tweet
    post_tweet(twitter_api, tweet_content)
