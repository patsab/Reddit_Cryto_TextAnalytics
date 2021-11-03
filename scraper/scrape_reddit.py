import praw
import sqlite3
import datetime
import pandas as pd
import reddit_auth_config as auth_cfg
import reddit_data_config as data_cfg


#auth info for accessing reddit
# specified in seperate config file
reddit = praw.Reddit(
    client_id=auth_cfg.client_id,
    client_secret=auth_cfg.client_secret,
    password=auth_cfg.password,
    user_agent=auth_cfg.user_agent,
    username=auth_cfg.username
)
# connection can be tested with the following line
# if done correctly, your username will be printed
#print(reddit.user.me())

#get the subreddits from the config file
subreddits = data_cfg.subreddits

data = []
#for each subreddit, the number of post from hot should be saved into the "data"-List
for sub in subreddits:
    subred = reddit.subreddit(sub)
    #subred.hot return posts sorted by hot
    for post in subred.top('year',limit = data_cfg.number_of_posts):
        post_data = {}
        post_data['subreddit'] = sub
        post_data['author'] = str(post.author)
        post_data['title'] = str(post.title)
        post_data['text'] = post.selftext
        post_data['upvotes'] = post.ups
        post_data['downvotes'] = post.downs
        post_data['category'] = post.link_flair_text
        post_data['creation_time'] = datetime.datetime.fromtimestamp(post.created_utc)
        data.append(post_data)

#create a pandas dataframe from the data
data_df = pd.DataFrame(data)

#save the data to a sqllite file
con = sqlite3.connect(data_cfg.output_path)
data_df.to_sql("post_data", con, if_exists="replace")
con.close()

