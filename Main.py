#Initial commit to make sure git is working
import getpass
from selenium import webdriver
from selenium import *
def initialize():
    try:
        driver = webdriver.Chrome("/Users/chromedriver")
        driver.get("https://boss.latech.edu")
        print("Opening chrome and navigating to Boss")
    except:
        print("The function 'initialize()' did not run successfully.")

initialize()

# #Takes input from the console or command line
# username = raw_input("Enter your student login in the format XXXXXXX: ")
# #Takes input from the console or command line and hides it so no one sees the password
# password = getpass.getpass("Enter your password: ")
