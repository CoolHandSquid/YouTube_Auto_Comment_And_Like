#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import calendar
from datetime import date
import time

channel_url	= "https://www.youtube.com/channel/UCsTKuPfW15Zu8lVa1gDqlNQ"
my_comment = "What a shame we fund this."
like = False #False will dislike the video. True will like the video

def comment(like):
	options = Options()
	#options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('user-data-dir=/root/.config/google-chrome')
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
	driver.get(channel_url)
	link_button = driver.find_element_by_xpath('(//*[@id="video-title"])[1]')
	link_button.click()
	time.sleep(1)
	elem = driver.find_element_by_tag_name('html')
	time.sleep(1)
	for i in range(10):
		elem.send_keys(Keys.DOWN)

	#if "like" Hit dislike first and then dislike. This eliminates the possibility of double likeing something (which makes the action NULL)
	time.sleep(1)
	if like == True:
		i = 2
		link_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[{}]/a'.format(i))
		link_button.click()
		time.sleep(1)
		i = 1
		link_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[{}]/a'.format(i))
		link_button.click()
	else:
		i = 1
		link_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[{}]/a'.format(i))
		link_button.click()
		time.sleep(1)
		i = 2
		link_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[{}]/a'.format(i))
		link_button.click()

	time.sleep(1)
	link_button = driver.find_element_by_xpath('//*[@id="placeholder-area"]')
	link_button.click()
	comment = driver.find_element_by_xpath('//*[@id="contenteditable-root"]')
	comment.send_keys(my_comment)
	link_button = driver.find_element_by_xpath('//*[@id="submit-button"]/a')
	link_button.click()

def main():
	print("Commenting on and like-or-dislikng the newest video on {}".format(channel_url))
	comment(like)
	#input("YEE")
main()
#f12, ctrl+ shift+c, click where you want to locate, rightclick in the analyzer, copy > copy xpath ### to find xpath
