#Initial commit to make sure git is working
import getpass
from selenium import webdriver

driver = webdriver.Chrome("/Users/dcr/Downloads/chromedriver")
driver.get("https://boss.latech.edu")

#Takes input from the console or command line
username = raw_input("Enter your student login in the format XXXXXXX: ")
#Takes input from the console or command line and hides it so no one sees the password
password = getpass.getpass("Enter your password: ")

