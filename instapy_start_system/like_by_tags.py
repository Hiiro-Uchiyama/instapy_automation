import random
from instapy import InstaPy
from instapy import smart_run

insta_username = 'USERNAME'
insta_password = 'PASSWORD'

dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch']

friends = ['フォローを外さないユーザー']

like_tag_list = ['いいねするハッシュタグ']

ignore_list = ['除外するハッシュタグ']

accounts = ['accounts with similar content']

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=None)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    max_followers=15000)
    # session.set_dont_include(friends)
    # session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)
    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=20)
    session.set_do_like(enabled=True, percentage=100)
    session.like_by_tags(random.sample(like_tag_list, 9),
                         amount=random.randint(60, 100), interact=True)
    # session.unfollow_users(amount=random.randint(75, 150),
    #                       InstapyFollowed=(True, "all"), style="FIFO",
    #                       unfollow_after=90 * 60 * 60, sleep_delay=501)
    # photo_comments = ['Nice shot! @{}',
    #     'I love your profile! @{}',
    #     'Wonderful :thumbsup:',
    #     'Just incredible :open_mouth:',
    #     'What camera did you use @{}?',
    #     'Love your posts @{}',
    #     'Looks awesome @{}',
    #     'Getting inspired by you @{}',
    #     ':raised_hands: Yes!',
    #     'I can feel your passion @{} :muscle:']
    # session.set_do_comment(enabled = True, percentage = 95)
    # session.set_comments(photo_comments, media = 'Photo')
    # session.join_pods(topic='travel')