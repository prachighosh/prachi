import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        :"YJBI68mqlAB5La7VgMJXs8kTf",
    "consumer_secret"     :"hvBRzme6CLenjLaoMQRRfHXLLUYVLrMSV1Xlsiq56ppmWKONsv"
,
    "access_token"        :"968053303388106753-n8nyI1NouUHtRQT5ZOc2K5zaqsVU4wr",
    "access_token_secret" :"iPRZhzGcb5wgGmathKrFEoLBoKdh7tEucbWMrrLLfxXo8"
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
