from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import numpy as np

# 1. Assign browser variable
browser  = webdriver.Chrome(executable_path="./chromedriver")


# 2. Open a webpage
browser.get("https://www.facebook.com/groups/voz.congnghe/permalink/716244449175823/")
sleep(5)

# 3. Assign
show_comment_btn = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span/a")
show_comment_btn.click()
sleep(random.randint(5,10))

show_more_btn = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[3]/div[1]/div/a")
show_more_btn.click()
sleep(random.randint(5,10))


# 4. Fetch comment list
comment_list = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")


# 5. Lặp trong tất cả các comment và hiển thị nội dung comment ra màn hình
for comment in comment_list:
    # hiển thị tên người và nội dung, cách nhau bởi dấu :
    poster = comment.find_element_by_class_name("_6qw4")
    content = comment.find_element_by_class_name("_3l3x")
    print("* {} : {}".format(poster.text, content.text))
sleep(random.randint(5,10))


browser.close()