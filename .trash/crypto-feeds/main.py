# import psycopg2

# conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")

# cur = conn.cursor()

# cur.execute(
# """
# CREATE TABLE IF NOT EXISTS feeds (
#     lunar_id VARCHAR(50) PRIMARY KEY,
#     symbol VARCHAR(50),
#     name VARCHAR(50),
#     time TIMESTAMP,
#     social_score INT,
#     type VARCHAR(50),
#     id VARCHAR(50),
#     title VARCHAR(50),
#     body TEXT,
#     subreddit TEXT,
#     commented INT,
#     likes INT,
#     link VARCHAR(50),
#     url VARCHAR(50)
# );
# """)

# x = str({'lunar_id': 2717960986, 'asset_id': 2780, 'symbol': 'DOT', 'name': 'Polkadot', 'time': 1627391424, 'social_score': 76, 'type': 'reddit', 'id': 'osmj3b', 'title': '5 Best Places to Stake Polkadot, IMHO', 'body': '', 'subreddit': 'dot', 'commented': 58, 'likes': 76, 'link': 'https://i.redd.it/p92q0s1j8rd71.jpg', 'url': 'https://www.reddit.com/r/dot/comments/osmj3b/'})

# cur.execute("insert into feeds select * from json_populate_record(NULL::feeds, '{}');".format(x))

# cur.execute("SELECT * FROM feeds;")
# a = cur.fetchall()
# print(a)

# cur.close()

######################################


import requests
import pandas as pd

# 20 Most popular info about DOT coin in July 2021 from Reddit
url = "https://api.lunarcrush.com/v2?data=feeds&key=e6v15bc92543jp0vbppl48&symbol=DOT&limit=20&start=1627366726&end=1627664400&sources=reddit,news"

df = pd.read_json(url)
print(df.head())

req = requests.get(url)

data = req.json()['data']

a = dict(data[0])
print(a.keys())

for key in a.keys():
    print(key, type(a[key]))

for item in data:
    print(item)

print(len(data))

