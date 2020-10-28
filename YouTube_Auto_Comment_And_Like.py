#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import calendar
from datetime import date
import time

channel_url	= "https://www.youtube.com/channel/UCsTKuPfW15Zu8lVa1gDqlNQ"
#video_name = "Tuesday October 27, 2020"	#Commented out because the get_name variable covers this for my useage
my_comment = "Another bias broadcast by NPR Up First. It is a shame that we fund this."
like = False #False will dislike the video. True will like the video

def get_name():
	global video_name, video_name2
	my_date = date.today()
	wday 	= str(calendar.day_name[my_date.weekday()])
	year 	= str(my_date.year)
	day 	= str(my_date.day)
	month 	= str(calendar.month_name[my_date.month])
	video_name 	= "{}, {} {} {}".format(wday, month, day, year)
	return video_name

def comment(video_name, like):
	options = Options()
	#options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('user-data-dir=/root/.config/google-chrome')
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
	driver.get(channel_url)
	link_button = driver.find_element_by_link_text(video_name)
	link_button.click()
	time.sleep(1)
	elem = driver.find_element_by_tag_name('html')
	time.sleep(1)
	for i in range(10):
		elem.send_keys(Keys.DOWN)

	time.sleep(1)
	if like == True:
		i = 1
	else:
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
	get_name()
	print("Commenting on and like-or-dislikng {}".format(video_name))
	comment(video_name, like)
	#input("YEE")
main()
#f12, ctrl+ shift+c, click where you want to locate, rightclick in the analyzer, copy > copy xpath ### to find xpath


