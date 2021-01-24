import requests
import json
import sys
import emoji
import MeCab
from datetime import datetime
from wordcloud import WordCloud
from settings import *


def main(keyword: str):
    remove_emoji_keyword = remove_emoji(keyword)  # type: str
    tweet_list = fetch_tweet_list(remove_emoji_keyword)  # type: list
    noun_list = extract_noun(tweet_list)  # type: list
    create_word_cloud(noun_list)


def remove_emoji(src_str: str) -> str:
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)


def fetch_tweet_list(keyword: str) -> list:
    max_results = "100"  # type: str
    header = {"Authorization": "Bearer " + BEARER_KEY}  # type: dict
    tweet_list = []  # type: list
    next_token = ""  # type: str
    for i in range(TWEET_COUNT):
        endpoint_url = "https://api.twitter.com/2/tweets/search/recent?query={}&max_results={}" \
            .format(keyword, max_results)  # type: str
        if i >= 1:
            endpoint_url = endpoint_url + "&next_token={}".format(next_token)
        response = json.loads(requests.get(url=endpoint_url, headers=header).text)  # type: json

        for data in response["data"]:
            tweet_list.append(data["text"])

        try:
            next_token = response["meta"]["next_token"]
        except KeyError:
            print(KeyError)

    return tweet_list


def extract_noun(text_list: list) -> list:
    noun_list = []  # type: list
    try:
        tagger = MeCab.Tagger("-d " + MECAB_DICT_PATH)
        print("mecab_dict=" + MECAB_DICT_PATH)
    except RuntimeError:
        tagger = MeCab.Tagger()
        print("mecab_dict=None")

    for text in text_list:
        text = remove_emoji(text)
        parse = tagger.parse(text)
        word = parse.split("\t")[0]
        if word == "EOS":
            break
        else:
            pos = parse.split("\t")[1]
            speech = pos.split(",")[0]
            if speech == "名詞":
                noun_list.append(word)
    return noun_list


def create_word_cloud(noun_list: list):
    stop_words = ["RT", "@", 'もの', 'こと', 'とき', 'そう', 'たち', 'これ', 'よう', 'これら', 'それ', 'すべて',
                  'https']  # type: list
    word_chain = ' '.join(noun_list)
    word_cloud = WordCloud(background_color="white", font_path=FONT_PATH, contour_color='steelblue',
                           collocations=False,
                           contour_width=3, width=900, height=500,
                           stopwords=set(stop_words)).generate(word_chain)
    file = datetime.today().strftime("%Y%m%d%H%M%S")
    word_cloud.to_file("./word_cloud/wc_" + file + ".png")
    print("export_image=./word_cloud/wc_" + file + ".png")


if __name__ == "__main__":
    input_word = sys.argv  # type: list
    main(input_word[1])
