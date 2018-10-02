import got3
import pandas as pd
tweetCriteria1 = got3.manager.TweetCriteria()
tweetCriteria1.setQuerySearch("samsung galaxy")
tweetCriteria1.setSince("2017-01-01")
tweetCriteria1.setUntil("2017-07-01")
tweetCriteria1.setMaxTweets(5000)
samsung_tweets = got3.manager.TweetManager.getTweets(tweetCriteria1)
print(len(samsung_tweets))
tweet_data=[]
for tweet in samsung_tweets:
  tweet_data.append((tweet.text,tweet.username,tweet.author_id,tweet.favorites,tweet.retweets,tweet.date,tweet.geo,tweet.mentions.split(),tweet.hashtags.split(),0))
tweetCriteria2 = got3.manager.TweetCriteria()
tweetCriteria2.setQuerySearch("iphone")
tweetCriteria2.setSince("2017-01-01")
tweetCriteria2.setUntil("2017-07-01")
tweetCriteria2.setMaxTweets(5000)
iphone_tweets = got3.manager.TweetManager.getTweets(tweetCriteria2)
print(len(iphone_tweets))
for tweet in iphone_tweets:
  tweet_data.append((tweet.text,tweet.username,tweet.author_id,tweet.favorites,tweet.retweets,tweet.date,tweet.geo,tweet.mentions.split(),tweet.hashtags.split(),1))

tweet_df=pd.DataFrame(tweet_data)
tweet_df.columns=["Tweet","username","author_id","favorites","retweets","date","geo","mentions","hashtags","Label"]
tweet_df.index=tweet_df["Tweet"]
del tweet_df["Tweet"]
tweet_df.to_csv("consolidatedtweets.csv")