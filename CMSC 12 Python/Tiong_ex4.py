"""This program will unlock the secret message using a security PIN."""
# John Vincent Tiong B-1L (Oct. 3, 2023)
# Submitted to Asst. Prof Carlo Tumibay

securityPin = None
secretMessage = "Why am I so handsome? haist di ko rin alam :<"

def menu():
    #This will print the menu and will ask the user for a choice
    print("MENU")
    print("[0] Exit Program")
    print("[1] Unlock Secret Message")
    print("[2] Change Security Pin")
    num = int(input("Choice "))
    return num

def secret_message(securityPin):
    #It will check if there is a Security PIN, if none, then it will ask for a PIN
    if securityPin is None:
        print("No Security PIN!")
        while securityPin is None:
            newpin = input("Enter New PIN (length of 4): ")
            if not newpin.isalnum() or not len(newpin) == 4:
                print("Invalid PIN!")
            else:
                securityPin = newpin
                print("Security PIN enabled!")
                return securityPin
    #If there is a PIN, it will ask for a PIN to validate
    else:
        #If PIN is correct, it will print the secret message
        inputPin = input("Enter PIN: ")
        if inputPin == securityPin:
            print (secretMessage)
            return securityPin
        else:
        #If PIN is not correct, it will not print the secret message
            print ("Entered PIN is incorrect")
            return securityPin

#It will allow the user to change the PIN
def manage_pin(securityPin):
    #It will check if there is a Security PIN, if none, then it will ask for a PIN
    if securityPin is None:
        print("No Security PIN!")
        while securityPin is None:
            newpin = input("Enter New PIN (length of 4): ")
            if not newpin.isalnum() or not len(newpin) == 4:
                print("Invalid PIN!")
            else:
                securityPin = newpin
                print ("Entered PIN is incorrect")
                return securityPin
    #If there is a PIN, it will ask for a PIN to validate
    else:
        #If PIN is correct, it will allow the user to change the PIN
        inputPin = input("Enter PIN: ")
        if inputPin == securityPin:
            managing_pin = True
            while managing_pin:
                newpin = input("Enter New PIN (length of 4): ")
                if not newpin.isalnum() or not len(newpin) == 4:
                    print("Invalid PIN!")
                else:
                    securityPin = newpin
                    print("Security PIN changed!")
                    return securityPin
        #If PIN is not correct, it will not allow the user to change the PIN       
        else:
            print ("Entered PIN is incorrect")
            return securityPin

# Main
running = True
while running:
    choice = menu()
    if choice == 0:
        running = False
    elif choice == 1:
        securityPin = secret_message(securityPin)
    elif choice == 2:
        securityPin = manage_pin(securityPin)
    else:
        print("Invalid choice. Please select a valid option")
