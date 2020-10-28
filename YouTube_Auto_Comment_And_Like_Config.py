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

"""
cd /opt
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install gdebi-core
gdebi google-chrome-stable_current_amd64.deb
python3 -m pip install selenium
wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
ln -sf /opt/chromedriver /usr/bin/chromedriver
"""

def init_persistant_cookie():
	options = Options()
	#options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('user-data-dir=/root/.config/google-chrome')
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
	driver.get(channel_url)
	input('Be sure to put log in to have the persistant cookie saved\n')
	os.system('killall chrome')

def main():
	os_init()
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.common.keys import Keys
	init_persistant_cookie()

main()