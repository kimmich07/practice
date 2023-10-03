#This program will unlock the secret message using a security PIN.
#by John Vincent Tiong of B-1L (Oct. 3, 2023)
#submitted to Asst. Prof Carlo Tumibay

securityPin = None
secretMessage = "Why am I so handsome? haist di ko rin alam :<"

def menu():
	#This will show the menu and will ask the user for his/her choice
    print("MENU")
    print("[0] Exit Program")
    print("[1] Unlock Secret Message")
	print("[2] Change Security Pin")
	#Insert choice
	num = int(input("Choice "))
	return num 

def secret_message(securityPin):
	#This will ask for the PIN to reveal the secret message
	if securityPin is None:
		print("No Security PIN!")
		while securityPin is None:
			newpin = int(input("Enter New PIN (length of 4): "))
			if not newpin.isalnum() or not len(newpin) == 4:
			 print("Invalid PIN!")
			else:
				securityPin = newpin
				print("Security PIN enabled!")
				return securityPin
	else:
		#If PIN is correct, it will print the secret message			
		inputPin = int(input("Enter PIN: "))
		if inputPin == securityPin:
			print (secretMessage)
			return securityPin
		#If PIN is not correct, it will not print the secret message
		else:
			print ("Entered PIN is incorrect")
			return securityPin


def manage_pin(securityPin):
	#This will allow the user to manage PIN
	if securtiyPin is None:
		print("No Security PIN!")
		while securityPin is None:
			newpin = int(input("Enter New PIN (length of 4): "))
			if not newpin.isalnum() or not len(newpin) == 4:
				print("Invalid PIN!")
			else:
				securityPin = newpin
				print ("Entered PIN is incorrect")
				return securityPin
	#If the PIN is correct, it will ask to change the PIN
	else:
		inputPin = int(input("Enter PIN: "))
		if inputPin == securityPin:
			manage_pin = True
			while manage_pin:
				newpin = int(input("Enter New PIN (length of 4): "))
				if not newpin.isalnum() or not len(newpin) == 4:
					print("Invalid PIN!")
				else:
					securityPin = newpin
					print ("Security PIN has been changed!")
					return securityPin
		#If PIN is not correct, it will not change the security PIN
		else:
			print("Entered PIN is incorrect")
			return securityPin
		return securityPin
	

#Main
running = True 
while running:
	choice = menu ()
	if choice == 0:
		running = False
		print("See you next time!")
	elif choice == 1:
		securityPin = secret_message(securityPin)
	elif choice == 2:
		securityPin = manage_pin(securityPin)
	else:
		print("Invalid choice. Please select a valid option")