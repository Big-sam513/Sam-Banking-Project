import time
from . import constant

def check_balance():
    constant.attempt = 0
    # pin = pin
    while constant.attempt < 3:
        user_pin = input("Enter your 4-digit pin to continue: ")
        if user_pin == constant.pin:
            print("PIN VERIFICATION SUCCESSFUL!!!")
            print("Procesing....")
            time.sleep(3)
            print(f"Your balance is {constant.balance}")
            break
        else:
            print(f"You have entered an invalid pin, You have {3-constant.attempt} attempt remaining.")
            constant.attempt += 1
    else:
        print("You Account has been temporary locked, Kindly visit the nearest UBA bank.")


def social():
    print("Follow me on my socials. Select an option below:\n")
    print("A. Sam Instagram\nB. Sam Facebook")

