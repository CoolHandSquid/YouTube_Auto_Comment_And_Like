#!/usr/bin/python3
import os

def os_init():
	os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
	os.system("apt install gdebi-core")
	os.system("gdebi google-chrome-stable_current_amd64.deb")
	os.system("python3 -m pip install selenium")
	os.system("wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip")
	os.system("unzip chromedriver_linux64.zip")
	os.system("ln -sf {}/chromedriver /usr/bin/chromedriver".format(os.getcwd()))

def init_persistant_cookie():
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.common.keys import Keys

	options = Options()
	#options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('user-data-dir=/root/.config/google-chrome')
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
	driver.get('https://mail.google.com')
	input('Once you have logged into gmail, hit ENTER.\n')
	input("You should be good to go to run YouTube_Auto_Comment_And_Like_Config.py!\nBe sure to edit the file to implement your comment, site, video, and whether to like or dislike.")
	os.system('killall chrome')

def main():
	os_init()
	init_persistant_cookie()

main()
