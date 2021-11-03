#testscript for testing if the sqllite db was created correctly
import sqlite3
import pandas as pd
import reddit_data_config as data_cfg

con = sqlite3.connect(data_cfg.output_path)
df = pd.read_sql_query("SELECT * from post_data", con)
con.close()

#print some stats of the data 
print(df.head())
print("Anzahl aller Elemente: {0}".format(len(df)), '\n')
for elemen in data_cfg.subreddits:
    print("Anzahl der Elemente in Subreddit '{0}' : {1}".format(elemen,df[df.subreddit == elemen].shape[0]) )


