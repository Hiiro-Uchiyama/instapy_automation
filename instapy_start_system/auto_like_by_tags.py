import random
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

insta_username = 'USERNAME'
insta_password = 'PASSWORD'

set_workspace(path=None)

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=None)

like_tag_list = ["いいねするハッシュタグ"]

with smart_run(session):
   # general settings
   # Excluding friends 
   # will prevent commenting on and unfollowing your good friends (the images will still be liked)
   # session.set_dont_include(["friend1", "friend2", "friend3"])
   # 実行（以下にイイネしたいタグ名を入力します、●●にはイイネする回数を入力します)
   session.set_user_interact(amount=2,randomize=True,percentage=60,media='Photo')
   session.set_do_like(enabled=True,percentage=80)
   session.like_by_tags(random.sample(like_tag_list, 3),amount=random.randint(50, 100),interact=True)
   #tags: The tags that will be searched for and posts will be liked from
   #amount: The amount of posts that will be liked
   #実行にあたっては以下のURLを参照
   #https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md#like-by-tags