"""Core banking operations and workflows."""
from typing import List
import time
import random
import datetime

from . import constant
# from . app import main



def check_bvn():
    while True:
        bvn = input("Enter your Bank Verification Number (BVN) below:\n ")
        if not bvn.isdigit():
            print("BVN must only contain numbers")
        elif len(bvn) != 11:
            print("Incomplete, BVN must exactly be 11 digits")
        else:
            print("BVN VERIFICATION SUCCESSFULLY...")
            return bvn


def check_phone():
    while True:
        pho_number = input("Enter Phone Number: \n")
        if not pho_number.isdigit():
            print("Your Phone Number must only contain numbers")
        elif len(pho_number) != 11:
            print("Incomplete, Phone Number must exactly be 11 digits")
        else:
            print("PHONE NUMBER VERIFIED....")
            return pho_number


def first_name():
    while True:
        fname = input("Enter Your First Name:\n " )
        if not fname.isalpha():
            print("First Name must only contain Alphabets")
        else:
            print("First Name VERIFIED....")
            return fname


def middle_name():
    while True:
        mname = input("Enter Your Middle Name: \n" )
        if not mname.isalpha():
            print("First Name must only contain Alphabets")
        else:
            print("First Name VERIFIED....")
            return mname


def last_name():
    while True:
        lname = input("Enter Your Last Name:\n " )
        if not lname.isalpha():
            print("First Name must only contain Alphabets")
        else:
            print("First Name VERIFIED....")
            return lname


def dob():
    while True:
        dob = input("Enter Date of Birth(DD/MM/YYYY):\n ")
        if dob.isalpha():
            print("DATE OF BIRTH CAN ONLY CONTAIN DIGIT NUMBERS.")
        elif "/" not in dob:
            print("KINDLY USE THE FORMAT, DATE OF BIRTH MUST CONTAIN '/' ")
        else:
            print("DATE OF BIRTH VERIFIED...")
            return dob


def address():
    while True:
        address = input("Enter Physical Address: \n")
        if not address.isalpha():
            print("ADDRESS must only contain Alphabets")
        else:
            print("ADDRESS VERIFIED....")
            return address


def email():
    while True:
        email = input("Enter Email Address:\n ")
        if "@" not in email:
            print("EMAIL ADDRESS MUST CONTAIN '@'")
            continue
        elif "." not in email:
            print("EMAIL MUST CONTAIN .")
            continue
        elif " " in email:
            print("EMAIL ADDRESS CANNOT CONTAIN SPACES")
            continue
        elif email.startswith("@") or email.endswith("@"):
            print("INVALID EMAIL FORMAT.")
            continue
        else:
            print("EMAIL ADDRESS VERIFIED....")
            return email


def bvn():
    
    global dob,address,email
    account_number: List[int] = []
    bvn = check_bvn()
    pho_number = check_phone()
    fname = first_name()
    mname = middle_name()
    lname = last_name()
    dob = dob()
    address = address()
    eaddress = email()
    while True:
        print("An Activation Code has been sent to your phone.Please reply this message with 4-digit code that will be sent to you:")
        otp = random.randint(1000 , 9999)
        print("Processing......")
        time.sleep(3)
        print("===================================")
        print(f"Your Activation Code is {otp}")
        print("===================================")
        print("\nThis code can only be used for one session. Please do not share. ")
        otp_input = int(input("\nEnter the OTP digit sent to you: "))
        if otp_input == otp:
            print("NUMBER VERIFED SUCCESSFULLY")
            print("Please confirm your details:\n")
            print(f"Mobile Number: {pho_number}\n")
            print(f"FirstName: {fname}\n")
            print(f"MiddleName: {mname}\n")
            print(f"LastName: {lname}\n")
            print(f"Date od Birth: {dob}\n")
            print(f"Physical Address: {address}\n")
            print(f"Email Address: {eaddress}\n")
            acc_details = input("Are they correct? yes/no: ").lower()
            if acc_details == "yes":
                print("Your Account Number is being Processed, It will be done shortly....")
                print("Processing......")
                time.sleep(5)
                for _ in range(10):
                    acc_num = random.choice(range(1, 11))
                    account_number.append(acc_num)
                print("Your account number is ")
                print("=============================")
                for x in account_number:
                    print(x, end="")
                print("\nThank you for banking with SAM.")
                print("==============================")
                break
                
            else:
                print("❌Let's try Again!!!")
                account_opening()
        else:
            print("Invalid Activation Code provided.Please try again.\nFor enquires, please call CFC at 02-012808822 or send an email to cfc@samgroup.com\n")
            break


def account_opening():
    open = True
    while open:
        print("We take your privacy seriously and only process your personal information to make your banking experience better.\nPlease read our privacy policy at www.samgroup.com before proceeding to use this platform. In accordance with NDPA, GDPR, and other applicable regulations.\nContinuing to use this platform indicates your consent to the collection and processing of your personal data by Sam Bank for Africa PLC, \nit's subsidiaries and partners,as detailed in Privacy Policy.\n")
        print("""
        A. Accept 
        B. Reject
            """)
        account_choice = input("Enter your choice(A/B): ").upper()
        if account_choice == "A":
            print("Great you decided to start a relationship with us.\nI will walk you through each step and i promise it would be super easy. Your account would be ready immediately! ")
            print("Do you have a Bank Verification Number(BVN)? \n")
            print("""
                  A.YES
                  B.NO
                  C.What is BVN?
                  """)
            bvn_choice = input(("Enter your Choice: ")).upper()
            if bvn_choice == "A":
                bvn()
                break
            elif bvn_choice == "B":
                print("You need a BVN to continue the account opening process.\n")
                print("If you do not have a BVN, you can enrol at any SAM branch.If you are outside Nigeria. Click the button below to locate global BVN enrolment centres")
                print("Thank You !!!")
                break
            elif bvn_choice == "C":
                print("The BVN is an 11 digit number that acts as your Universal ID in all banks in Nigeria.\n")
                print("If you have a bank account with another bank in Nigeria. You can get your BVN.\n")
                print("Do You have a BVN?\n")
                print(""" 
                A. YES
                B. NO
                C. Quit
                      """)
                choice = input("Enter your choice (A-C): ").upper()
                if choice == "A":
                    bvn()
                elif choice =="B":
                    print("You need a BVN to continue the account opening process.\n")
                    print("If you do not have a BVN, you can enrol at any SAM branch.If you are outside Nigeria. Click the button bellow to locate global BVN enrolment centres")
                    print("Thank You !!!")
                    break
                else:
                    print("Thank You !!!")
                    break
        else:
            return


def airtime():
    attempt = 0
    airtime = True
    while airtime:
        print("Please select the number you want to recharge from the list or enter a new number:")
        print("""
                A. ME
                B. NEW NUMBER
            """)
        airtime_choice = input("Enter your choice (A/B): ").upper()
        if airtime_choice == "A":
            try:
                airtime_amount = int(input("How much do you want to recharge? \n"))
            except ValueError:
                print("Invalid Input")
                continue
            else:
                print("Valid Input.")
            print("If this is okay,respond with PAY or respond with CANCEL terminate this process.\n")
            print("Network: AIRTEL")
            print("Phone number: 2347014601541")
            print(f"Amount: ₦ {airtime_amount}\n")
            print("""
                  A.PAY
                  B.CANCEL
                  """)
            airtime_choice2 = input("Enter your choice (A/B): ").upper()
            if airtime_choice2 == "A":
                while attempt < 3:
                    airtime_pin = input("Enter Your 4-digit pin: ")
                    if airtime_pin == constant.pin:
                        print("PIN VERIFIED SUCCESSFULLY")
                        print("Processing......")
                        time.sleep(5)
                        print("====================================================")
                        print(f"You have successfully purchased an Airtime of ₦{airtime_amount}")
                        print("====================================================")
                        airtime = False
                        break
                    else:
                        print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                        attempt += 1
                        continue
                else:
                    print("You have used all your attempt, Kindly reset your pin.")
                    break
            else:
                return
        elif airtime_choice == "B":
            num = input("Enter the number you want to recharge: ")
            if not num.isdigit():
                print("Invalid Input.")
                continue
            elif len(num) != 11:
                print("Incomplete, Numbers must contain 11 digit.")
                continue
            else:
                print("Number Verified...")
            print("Kindly enter the network operator: ")
            print("""
                    A. Airtel
                    B. MTN
                    C. GLO
                """)
            operator = input("Enter your choice (A-C): ").upper()
            if operator in {"A","B","C"}:
                airtime_amount = input("How much do you want to recharge: ")
                print("Valid Input")
                network = {"A":"AIRTEL","B":"MTN","C":"GLO"}[operator]
                print("If this is okay,respond with PAY or respond with CANCEL to terminate this process.\n")
                print(f"Network: {network}")
                print(f"Phone number: {num}")
                print(f"Amount: ₦ {airtime_amount}\n")
                print("""
                      A.PAY
                      B.CANCEL
                      """)
                airtime_choice2 = input("Enter your choice (A/B): ").upper()
                if airtime_choice2 == "A":
                    while attempt < 3:
                        airtime_pin = input("Enter Your 4-digit pin: ")
                        if airtime_pin == constant.pin:
                            print("PIN VERIFIED SUCCESSFULLY")
                            print("Processing......")
                            time.sleep(5)
                            print("========================================================")
                            print(f"You have successfully purchased an Airtime of ₦{airtime_amount}")
                            print("========================================================")
                            airtime = False
                            break
                        else:
                            print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                            attempt += 1
                            continue
                else:
                    return


