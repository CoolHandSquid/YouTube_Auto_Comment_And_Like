#!/usr/bin/python3
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from datetime import date
import time

channel_url = "https://www.youtube.com/channel/UCsTKuPfW15Zu8lVa1gDqlNQ"
like 		= False
my_comment	= "Not very Yeet at all"
Num_of_Videos	= 1 #How many videos do you want to write to? YouTube only allows 250 per channel per day


bstart 	= time.time()
Num_of_Videos += 1
options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-data-dir=/root/.config/google-chrome')
driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
driver.get(channel_url)
time.sleep(1)
elem = driver.find_element_by_tag_name('html')
for i in range(11):
	elem.send_keys(Keys.DOWN)
time.sleep(1)

for vn in range(1,Num_of_Videos):
	start = time.time()
	#open new tab, switch to it and prepare it logic
	driver.find_element_by_xpath('(//*[@id="video-title"])[{}]'.format(vn)).send_keys(Keys.CONTROL,Keys.RETURN)
	time.sleep(1)
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(1)
	elem = driver.find_element_by_tag_name('html')
	for i in range(10):
		elem.send_keys(Keys.DOWN)
#	input("did it scroll?")
	#like/dislike logic
	time.sleep(1)
	if like == True:
		l = 2
		link_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[{}]/a'.format(l))
		link_button.click()
		time.sleep(1)
		l = 1
		link_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[{}]/a'.format(l))
		link_button.click()
	else:
		l = 1
		link_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[{}]/a'.format(l))
		link_button.click()
		time.sleep(1)
		l = 2
		link_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[{}]/a'.format(l))
		link_button.click()
#	input("did it dislike?")
	#Comment logic
	time.sleep(2)
	link_button = driver.find_element_by_xpath('//*[@id="placeholder-area"]')
	link_button.click()
	time.sleep(1)
	comment = driver.find_element_by_xpath('//*[@id="contenteditable-root"]')
	comment.send_keys(my_comment)
	link_button = driver.find_element_by_xpath('//*[@id="submit-button"]/a')
	link_button.click()
	time.sleep(1)
#	input("did it comment?")
	#Scroll logic
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	elem = driver.find_element_by_tag_name('html')
	if vn % 6 == 1:
		for s in range(6):
			elem.send_keys(Keys.DOWN)
	else:
		pass
	end 		= time.time()
	vruntime 	= int((end - start))
	runtime 	= int((end - bstart))
	print("videos:{} vidtime:{} runtime:{}\n".format(vn, vruntime, runtime))
#	input("How are we doing?")
