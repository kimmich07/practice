"""This program will unlock the secret message using a security PIN."""
# John Vincent Tiong B-1L (Oct. 3, 2023)
# Submitted to Asst. Prof Carlo Tumibay

securityPin = None
secretMessage = "Why am I so handsome? haist di ko rin alam :<"

def menu():
    print("MENU")
    print("[0] Exit Program")
    print("[1] Unlock Secret Message")
    print("[2] Change Security Pin")
    num = int(input("Choice "))
    return num

def secret_message(securityPin):
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
    else:
        inputPin = input("Enter PIN: ")
        if inputPin == securityPin:
            print (secretMessage)
            return securityPin
        else:
            print ("Entered PIN is incorrect")
            return securityPin

def manage_pin(securityPin):
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
    else:
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
