import os
from twitter_bot_class import LinkedinBot

if __name__ == "__main__":
    try:
        pj = LinkedinBot('charulatha@gmail.com', 'Password@123')
        pj.login()
        pj.post_posts("My bot's first tweet!")
        pj.logout()
    except Exception as e:
        pj.logout()
        print(e)

