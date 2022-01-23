import requests
import xml.etree.ElementTree as ET
import random
import tweepy
import datetime

def tweet_random_post_title_and_link(tweet_message):
    # 認証に必要なキーとトークン
    API_KEY = 'XXXXXXXXXX'
    API_SECRET = 'XXXXXXXXXX'
    ACCESS_TOKEN = 'XXXXXXXXXX-XXXXXXXXXX'
    ACCESS_TOKEN_SECRET = 'XXXXXXXXXX'

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(tweet_message)

def get_random_post_title_and_link():
    url = "https://blog.hatena.ne.jp/katsu-ichiro/better-software-testing.hatenablog.com/atom/entry"

    payload={}
    headers = {
    'Authorization': 'Basic XXXXXXXXXX',
    'Cookie': 'b=XXXXXXXXXX; sk=XXXXXXXXXX'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    root = ET.fromstring(response.text)
    index = random.randint(0,9)
    entry = root.findall("{http://www.w3.org/2005/Atom}entry")[index]
    link = entry.findall("{http://www.w3.org/2005/Atom}link")[1].attrib['href']
    title = entry.find("{http://www.w3.org/2005/Atom}title").text
    post_info_dict = {
        "title": title,
        "link": link
    }
    return post_info_dict

post_info_dict = get_random_post_title_and_link()
print(post_info_dict["title"] + " : " + post_info_dict["link"])
today = datetime.date.today()
tweet_random_post_title_and_link(today.strftime('%Y年%m月%d日') + "のおすすめ" + post_info_dict["link"])