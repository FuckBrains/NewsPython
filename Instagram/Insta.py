from time import sleep

import geckodriver_autoinstaller
from selenium import webdriver

from instapy import InstaPy
from instapy import smart_run


session = InstaPy(username="horseofplaydom", password="Password@123", headless_browser= False, geckodriver_path="G:\\driver\\geckodriver.exe")


with smart_run(session):
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True,max_followers=500, min_followers=30, min_following=50)
    session.set_do_follow(True, percentage=100)
    session.set_dont_like(["naked", "nsfw"])
    session.like_by_tags(["news", "nation"], amount=10)
#session.login()




#session.set_do_comment(True, percentage=50)
#session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
#session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

#session.end()
