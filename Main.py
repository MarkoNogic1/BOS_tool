#Initial commit to make sure git is working
import getpass

#Takes input from the console or command line
username = raw_input("Enter your student login in the format XXXXXXX: ")
#Takes input from the console or command line and hides it so no one sees the password
password = getpass.getpass("Enter your password: ")