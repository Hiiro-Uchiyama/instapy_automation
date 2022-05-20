from instapy import InstaPy
from instapy import smart_run

insta_username = 'USERNAME'
insta_password = 'PASSWORD'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    nonfollowers = session.pick_nonfollowers(username=insta_username, live_match=True, store_locally=True)
    print(nonfollowers)
    session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=42 * 60 * 60, sleep_delay=655)