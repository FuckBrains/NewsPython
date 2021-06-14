import os
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), 'chromedriver'))
driver.maximize_window()

SAVE_PATH = "G:\\Videos\\"  # to_do

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Navigate to url with video being appended to search_query
driver.get('https://www.youtube.com/')

# play the video
wait.until(visible((By.ID, "search")))
driver.find_element_by_id("search").send_keys("HUMANITY")
driver.find_element_by_id("search-icon-legacy").click()

wait.until(visible((By.XPATH, "//div[@id='filter-menu']/div/ytd-toggle-button-renderer/a")))
driver.find_element_by_xpath("//div[@id='filter-menu']/div/ytd-toggle-button-renderer/a").click()

wait.until(visible((By.XPATH, "//yt-formatted-string[contains(text(), 'Creative Commons')]")))
driver.find_element_by_xpath("//yt-formatted-string[contains(text(), 'Creative Commons')]").click()



res=driver.find_elements_by_id("video-title")

for r in res:
    try:
        s = r.get_attribute("href")
        print(r.get_attribute("href"))
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(s)
        print(yt.title)
        print(yt.thumbnail_url)
        print(yt.title)
        print(yt.title)
        print("********************Download video*************************")
        # get all the stream resolution for the
        for stream in yt.streams:
            print(stream)

        # set stream resolution
        my_video = yt.streams.get_highest_resolution()


        try:
            # downloading the video
            my_video.download(SAVE_PATH)
        except:
            print("Some Error!")
    except:
        # to handle exception
        print("Connection Error")


    print('Task Completed!')


