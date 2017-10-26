#Initial commit to make sure git is working
import getpass
from selenium import webdriver
from selenium import *
import sys

#Keep driver global so it is accessible throughout the program
driver = webdriver.Chrome()
BossID = ""
BossPIN = ""
term = ""

#Takes input from the console or command line
def getUserName():
    global BossID
    BossID = input("Enter your student login in the format XXXXXXX: ")
    while(len(BossID) != 8):
        BossID = input("You did not enter an 8 digit student ID. Please enter your student login in the format XXXXXXX: ")
# #Takes input from the console or command line and hides it so no one sees the password
def getPassWord():
    global BossPIN
    BossPIN = getpass.getpass("Enter your password in the format XXXXXX: ")
def getTerm():
    global term
    term = input("Enter in the term in the format Quarter Year i.e Winter 2018: ")


def initialize():
    try:
        driver.get("https://boss.latech.edu")
        print("Opening chrome and navigating to Boss")
    except:
        print("The function 'initialize()' did not run successfully.")

def LogIn():
    driver.find_element_by_link_text("Student B.O.S.S. Login").click()
    elem = driver.find_element_by_name("SID")
    elem.clear()
    elem.send_keys(BossID)
    elem = driver.find_element_by_name("PIN")
    elem.clear()
    elem.send_keys(BossPIN)
    driver.find_element_by_name("submitbutton").click()

def DisplayMenu():
    print("What would you like to do?")
    print("[1] Select Term")
    print("[2] Check for Holds")
    print("[3] Exit Program")

    UserChoice = int(input())
    if(UserChoice == 1):
        SelectTerm()
    elif(UserChoice == 2):
        CheckForHolds()
    elif(UserChoice == 3):
        driver.close()
        sys.exit()
    else:
        print("You did not enter a valid option")

def CheckForHolds():
    driver.find_element_by_link_text("Holds").click()
    if ("You have no holds" in driver.page_source):
        print("You have no holds")
    else:
        print("You have a hold on your account")
    driver.find_element_by_link_text("SITE MAP").click()

def SelectTerm():
    driver.find_element_by_link_text("Select Term").click()
    driver.find_element_by_link_text(term).click()

getUserName()
getPassWord()
getTerm()
initialize()
LogIn()
while(True):
    print()
    DisplayMenu()

