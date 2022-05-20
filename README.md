## Instagram Automation

2022年5月19日現在動作確認ができているソースコードです。
Githubのissueを見ながらライブラリのエラー解消を行いました。

## コードの実行方法

InstaPyのソースフォルダがあるディレクトリへ移動し、InstaPyを置き換えます。
その後instapy_start_systemのディレクトリへ`cd .../〇〇/instapy_start_system`で移動し、コマンドから`python 〇〇`と任意のファイルを実行することで、InstaPyを実行することができます。

## 問題点

- 自動いいねプログラムを動かしていると下記のようなエラーが発生する場合がある

```
Traceback (most recent call last):
  File "like_by_tags.py", line 51, in <module>
    session.like_by_tags(random.sample(like_tag_list, 9),
  File "/Users/〇〇/opt/anaconda3/lib/python3.8/site-packages/instapy/instapy.py", line 1980, in like_by_tags
    inappropriate, user_name, is_video, reason, scope = check_link(
  File "/Users/〇〇/opt/anaconda3/lib/python3.8/site-packages/instapy/like_util.py", line 614, in check_link
    media = post_page['items'][0]
KeyError: 'items'
```

対策方法としては再度実行を行う、もしくはKeyErrorをキャッチして処理を飛ばすか、`items`という要素が見当たらないことから、InstagramのXPathを確認し、`items`とは異なる要素名を確認する。なお、現在はこのエラーに対する処理は記述できていない。

## ライブラリの修正方法

フォルダを検索する際に、任意のコマンドを入力し、上記のエラーで発生しているような`/Users/〇〇/opt/anaconda3/lib/python3.8/site-packages/instapy/like_util.py`を入力することで、指定のファイルにアクセスすることができます。MacOSであれば`command + shift + G``でパス検索を行うことができます。

## 仕様

1. [InstaPy](https://github.com/Hiiro-Uchiyama/instapy_automation/instapy/README.md)