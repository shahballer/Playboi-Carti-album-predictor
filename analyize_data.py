import pandas as pd
import matplotlib.pyplot as plt


tweets_df = pd.read_csv("CartiTweets.csv")
print("📊 Twitter Data Preview:")
print(tweets_df.head())

t
tweets_df["Timestamp"] = pd.to_datetime(tweets_df["Timestamp"])
tweets_df["Date"] = tweets_df["Timestamp"].dt.date  # Extract date only


tweet_counts = tweets_df["Date"].value_counts().sort_index()


plt.figure(figsize=(10, 5))
plt.plot(tweet_counts.index, tweet_counts.values, marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Number of Tweets")
plt.title("Playboi Carti's Tweet Frequency Over Time")
plt.xticks(rotation=45)
plt.show()


insta_df = pd.read_csv("CartiInstagram.csv")
print("\n📊 Instagram Data Preview:")
print(insta_df.head())


insta_df["Timestamp"] = pd.to_datetime(insta_df["Timestamp"])
insta_df["Date"] = insta_df["Timestamp"].dt.date


insta_counts = insta_df["Date"].value_counts().sort_index()


plt.figure(figsize=(10, 5))
plt.plot(insta_counts.index, insta_counts.values, marker='o', linestyle='-', color='red')
plt.xlabel("Date")
plt.ylabel("Number of Posts")
plt.title("Playboi Carti's Instagram Posting Frequency Over Time")
plt.xticks(rotation=45)
plt.show()
