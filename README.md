# twitter-wordcloud-generator

<img src="https://raw.githubusercontent.com/NekoSarada1101/twitter-wordcloud-generator/main/word_cloud/wc_20210124172249.png" width=600px>

## 概要

指定した単語を含むツイートでwordCloudを作成する。

## 開発環境

* Python 3.8
* [Twitter API](https://developer.twitter.com/en)
* [MeCab](https://taku910.github.io/mecab/)
* [WordCloud](http://amueller.github.io/word_cloud/index.html)

## 使用方法

リポジトリをクローンする。

```
git clone https://github.com/NekoSarada1101/twitter-wordcloud-generator.git
```

[settings.py](https://github.com/NekoSarada1101/twitter-wordcloud-generator/blob/main/settings.py)
のBEARER_KEYを自分のBearer keyに書き換える。

ディレクトリを移動し、実行する。

```
cd twitter-wordcloud-generator
python main.py {keyword}
```

### オプション

* MeCabで使用する辞書を変更する。  
  [settings.py](https://github.com/NekoSarada1101/twitter-wordcloud-generator/blob/main/settings.py)
  のMECAB_DICT_PATHを自分の辞書ファイルへのパスに書き換える。


* WordCloud生成に使うフォントを変更する。  
  [settings.py](https://github.com/NekoSarada1101/twitter-wordcloud-generator/blob/main/settings.py)
  のFONT_PATHを自分のフォントファイルへのパスに書き換える。


* WordCloud生成に使うツイートの数を変更する。  
  [settings.py](https://github.com/NekoSarada1101/twitter-wordcloud-generator/blob/main/settings.py)
  のTWEET_COUNTを取得したいツイートの数/100に書き換える。
