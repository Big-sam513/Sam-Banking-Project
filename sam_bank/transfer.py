import time
from . import constant



def send_money():
    global constant,benefit_name,masked,account_name,bank
    send = True
    attempt = 0
    service_fee = 10.75
    while send:
        print("Who do you want to send money to?\n")
        print(""" 
        A.New Account
        B.To Beneficiaries
        C.Download Beneficiaries
              """)
        money_choice = input("Enter your choice: ").upper()
        if money_choice == "A":
            while True:
                account = input("Enter Recipient Account Number: ")
                if account.isdigit() and len(account) == 10:
                    print("Account Number Saved...\n")
                    masked = ("*"*6 + account[-4:])
                    break
                else:
                    print("Invalid Input, Try Again.")
                    continue
            while True:
                account_name = input("Enter the Recipient Account Name: ")
                if not account_name.isalpha():
                    print("Invalid Account Name.")
                    continue
                else:
                    print("Account Name Saved....\n")
                    break
            while True:
                bank = input("Enter Bank Name: ")
                if not bank.isalpha():
                    print("Invalid Bank Name.")
                    continue
                else:
                    print("Bank Name Saved...\n")
                    break
            print("==========================================================")    
            print(f"Account number {masked} {account_name} is confirmed.")
            print("==========================================================") 
            while True:
                amount = input("How much do you want to transfer? ")
                if not amount.isdigit():
                    print("Invalid Input")
                    continue
                else:
                    print("Amount Saved...")
                    amount = int(amount)
                    constant.balance -= amount
                    constant.balance -= service_fee
                    break
            print("Enter the description for this transaction below or type skip: ")
            print("""
                  A.Skip
                  B.Continue
                  """)
            
            description = input("Enter your choice (A/B): ").upper()
            if description == "A":
                print("Please confirm the details below and respond with PAY if ok.\n")
                print("===================================================")
                print(f"Amount: ₦{amount}")
                print(f"Service Fee: ₦{service_fee}\n")
                print(f"Recipient: {masked} ({account_name})")
                print(f"Recipient Bank: {bank}")
                print("===================================================")
                print("""
                      A.PAY
                      B.EDIT
                      CANCEL
                      """)
        
                des_choice = input("Enter your choice: ").upper()
                if des_choice == "A":
                    while attempt < 3:
                        transfer_pin = input("Enter Your 4-digit pin: ")
                        if transfer_pin == constant.pin:
                            print("PIN VERIFIED SUCCESSFULLY")
                            print("Processing......")
                            time.sleep(5)
                            print("============================================================================")
                            print(f"You have successfully transferred ₦{amount} to {masked} {account_name}")
                            print(f"Your balance is ₦{constant.balance}")
                            print("============================================================================")
                            benefit = input("Will you like to add the recipient to your beneficiary? (y/n):").lower()
                            if benefit == "y":
                                benefit_name = input("Enter the beneficiary name: ")
                                constant.Beneficiary.append(benefit_name)
                                print("Beneficiary Added Successfully.....")
                            send = False
                            break
                        else:
                            print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                            attempt += 1
                            continue
                    else:
                        print("You have used all your attempt, Kindly reset your pin.")
                        return
                elif des_choice == "B":
                    continue
                else:
                    break

            elif description == "B":
                narration = input("Enter the description of the transfer: ")
                print("Please confirm the details below and respond with PAY if ok.\n")
                print("===================================================")
                print(f"Amount: ₦{amount}")
                print(f"Service Fee: ₦{service_fee}")
                print(f"Narration: {narration}\n")
                print(f"Recipient: {masked} ({account_name})")
                print(f"Recipient Bank: {bank}")
                print("===================================================")
                print("""
                      A.PAY
                      B.EDIT
                      C.CANCEL
                      """)

                des_choice = input("Enter your choice: ").upper()
                if des_choice == "A":
                    while attempt < 3:
                        transfer_pin = input("Enter Your 4-digit pin: ")
                        if transfer_pin == constant.pin:
                            print("PIN VERIFIED SUCCESSFULLY")
                            print("Processing......")
                            time.sleep(5)
                            print("=====================================================")
                            print(f"You have successfully transferred ₦{amount} to {masked} {account_name}")
                            print(f"Your balance is ₦{constant.balance}")
                            print("=====================================================")
                            benefit = input("Will you like to add the recipient to your beneficiary? (y/n):").lower()
                            if benefit == "y":
                                benefit_name = input("Enter the beneficiary name: ")
                                constant.Beneficiary.append(benefit_name)
                                print("Beneficiary Added Successfully.....")
                                # print(constant.Beneficiary)
                            send = False
                            break
            
                        else:
                            print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                            attempt += 1
                            continue
                    else:
                        print("You have used all your attempt, Kindly reset your pin.")
                        break
                elif des_choice == "B":
                    continue
                else:
                    break
            else:
                print("You Entered an Invalid Input")
                break

        elif money_choice == "B":
            if not constant.Beneficiary:
                print("No beneficiaries found...")
                print("Please Add a beneficiary...")
                break
            else:
                for i, benefit_name in enumerate(constant.Beneficiary, start=1):
                    print(f"{i}.{benefit_name}")
                B_name = input("Enter the beneficiary name: ")
                if B_name not in constant.Beneficiary:
                    print("Beneficiary does not exist")
                    break
                else:
                    print("Beneficiary Accessed....")
                while True:
                    amount = input("How much do you want to transfer? ")
                    if not amount.isdigit():
                        print("Invalid Input")
                        continue
                    else:
                        print("Amount Saved...")
                        amount = int(amount)
                        constant.balance -= amount
                        constant.balance -= service_fee
                        break
                print("Enter the description for this transaction below or type skip: \nA.Skip\nB.Continue")
                print("""
                        A. Skip
                        B. Continue
                    """)
                description = input("Enter your choice: ").upper()
                if description == "A":
                    while attempt < 3:
                        transfer_pin = input("Enter Your 4-digit pin: ")
                        if transfer_pin == constant.pin:
                            print("PIN VERIFIED SUCCESSFULLY")
                            print("Processing......")
                            time.sleep(5)
                            print(f"You have successfully transferred ₦{amount} to {masked} {account_name}")
                            print(f"Your balance is ₦{constant.balance}")
                            send = False
                            break
                        else:
                            print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                            attempt += 1
                            continue
                    else:
                        print("You have used all your attempt, Kindly reset your pin.")
                        break
                elif description == "B":
                    narration = input("Enter the description of the transfer: ")
                    print("Please confirm the details below and respond with PAY if ok.\n")
                    print("===================================================")
                    print(f"Amount: ₦{amount}")
                    print(f"Service Fee: ₦{service_fee}")
                    print(f"Narration: {narration}\n")
                    print(f"Recipient: {masked} ({account_name})")
                    print(f"Recipient Bank: {bank}")
                    print("===================================================")
                    print("""
                          A.PAY
                          B.EDIT
                          C.CANCEL
                          """)
                    des_choice = input("Enter your choice: ").upper()
                    if des_choice == "A":
                        while attempt < 3:
                            transfer_pin = input("Enter Your 4-digit pin: ")
                            if transfer_pin == constant.pin:
                                print("PIN VERIFIED SUCCESSFULLY")
                                print("Processing......")
                                time.sleep(5)
                                print("===========================================")
                                print(f"You have successfully transferred ₦{amount} to {masked} {account_name}")
                                print(f"Your balance is ₦{constant.balance}")
                                print("===========================================")
                                send = False
                                break
                            else:
                                print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                                attempt += 1
                                continue
                        else:
                            print("You have used all your attempt, Kindly reset your pin.")
                            break
        elif money_choice == "C":
            
            print("The List of your beneficiaries are: ")
            if not constant.Beneficiary:
                print("No Beneficiary Added..")
                break
            else:
                for i,  benefit_name in enumerate(constant.Beneficiary, start=1):
                    print(f"{i}. {benefit_name}")
                    break
                

