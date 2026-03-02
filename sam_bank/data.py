import time
from . import constant
from . import app

plans = {
    "A":{
        "name": "230MB Daily Plan",
        "price": 200,
        "validity": "1 day"
    },

    "B":{
        "name": "600MB+2mins+2SMS",
        "price": 500,
        "validity": "1 day",
    },

    "C":{
        "name": "1.8GB+6mins+5SMS",
        "price": 1500,
        "validity": "3 days",
    },

    "D": {
       "name": "2.7GB+15mins+5SMS",
        "price": 3000,
        "validity": "3 days", 
    },

    "E": {
        "name": "12.5GB+30mins+155SMS",
        "price": 5500,
        "validity": "7 days",
    },

    "F":{
        "name": "110MB",
        "price": 100,
        "validity": "1 days",
    },

    "G":{
        "name": "1.5GB+1GB YouTubeNight+100MB YoutubeMusic",
        "price": 1000,
        "validity": "3 days",
    },

    "H":{
        "name": "165GB SME Mobile Data",
        "price": "60,000",
        "validity": "2 months",
    },

    "I": {
        "name": "165GB Monthly Plan",
        "price": "35,000",
        "validity": "3 days",
    },

    "J": {
        "name": "11GB Weekly Bundle",
        "price": "3,500",
        "validity": "7 days",
    },

}




def buy_data():
    attempt = 0
    data = True
    while data:    
        print("Available Data Bundles:  \n")
        for key,value in plans.items():
            # print(key, value)
            print(f"{key}. {value["name"]} ---> ₦{value["price"]}")


        choice = input("Select your data bundle from the list below (A-J) :").upper()
        selected = plans.get(choice)
        if selected:
            print("===============================================")
            print(f"You selected {selected["name"]}")
            print(f"Price: ₦{selected["price"]}")
            print(f"Validity: {selected["validity"]}")
            print("===============================================\n")

            print("If this is okay, respond with PAY or respond with CANCEL to terminate this process.\n")
            print(f"Phone Number: {constant.number}\n")
            print(f"Bundle: {selected["name"]}\n")
            print(f"Amount: ₦{selected["price"]}\n")
            print("""
                A.PAY
                B.CANCEL
                """)
            choice1 = input("Enter your choice (A/B): ").upper()
            if choice1 == "A":
                while attempt < 3:
                    data_pin = input("Enter Your 4-digit pin: ")
                    if data_pin == constant.pin:
                        print("PIN VERIFIED SUCCESSFULLY")
                        print("Processing......")
                        time.sleep(5)
                        print("==============================================================")
                        print(f"You have successfully purchased {selected["name"]} Bundle valid for {selected["validity"]}")
                        print("THANK YOU FOR BANKING WITH SAM.")
                        print("==============================================================")
                        data = False
                        break
                    else:
                        print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                        attempt += 1
                        continue
                else:
                    print("You have used all your attempt, Kindly reset your pin.")
                    break

            else:
                print("THANKS FOR BANKING WITH SAM")
                app.main()


        else:
            print("Invalid Selection.")


def user():
    global attempt
    attempt = 0
    user = True
    while user:
        print("Select the number you want to buy data for or enter a new number")
        print("""
                A. ME
                B. New Number
            """)
        users_choice = input("Select your network(A/B): ").upper()
        if users_choice == "A":
            buy_data()
            break
        elif users_choice == "B":
            num = input("Enter the number you want to recharge: ")
            if not num.isdigit():
                print("Invalid Input.")
                continue
            elif len(num) != 11:
                print("Incomplete, Numbers must contain 11 digit.")
                continue
            else:
                print("Number Verified...")
            
            print("What network did you want to buy data for?")
            print("""
                A. MTN
                B. Airtel
                C. Glo
            """)
            operator = input("Enter the network operator (A-C): ").upper()
            if operator == "A":
                print("Available Data Bundles: \n")
                for key,value in plans.items():
            # print(key, value)
                    print(f"{key}. {value["name"]} ---> ₦{value["price"]}")


                choice = input("Select your data bundle from the list below (A-J) :").upper()
                selected = plans.get(choice)
                if selected:
                    print("===============================================")
                    print(f"You selected {selected["name"]}")
                    print(f"Price: ₦{selected["price"]}")
                    print(f"Validity: {selected["validity"]}")
                    print("===============================================\n")

                    print("If this is okay, respond with PAY or respond with CANCEL to terminate this process.\n")
                    print(f"Phone Number: {num}\n")
                    print(f"Bundle: {selected["name"]}\n")
                    print(f"Amount: ₦{selected["price"]}\n")
                    print("""
                        A.PAY
                        B.CANCEL
                        """)
                    choice1 = input("Enter your choice (A/B): ").upper()
                    if choice1 == "A":
                        while attempt < 3:
                            data_pin = input("Enter Your 4-digit pin: ")
                            if data_pin == constant.pin:
                                print("PIN VERIFIED SUCCESSFULLY")
                                print("Processing......")
                                time.sleep(5)
                                print("==============================================================")
                                print(f"You have successfully purchased {selected["name"]} Bundle valid for {selected["validity"]}")
                                print("THANK YOU FOR BANKING WITH SAM.")
                                print("==============================================================")
                                user = False
                                break
                            else:
                                print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                                attempt += 1
                                continue
                        else:
                            print("You have used all your attempt, Kindly reset your pin.")
                            break

                    else:
                        print("THANKS FOR BANKING WITH SAM")
                        app.main()


                else:
                    print("Invalid Selection.")

            elif operator == "B":
                print("Available Data Bundles: \n")
                for key,value in plans.items():
                    # print(key, value)
                    print(f"{key}. {value["name"]} ---> ₦{value["price"]}")


                choice = input("Select your data bundle from the list below (A-J) :").upper()
                selected = plans.get(choice)
                if selected:
                    print("===============================================")
                    print(f"You selected {selected["name"]}")
                    print(f"Price: ₦{selected["price"]}")
                    print(f"Validity: {selected["validity"]}")
                    print("===============================================\n")

                    print("If this is okay, respond with PAY or respond with CANCEL to terminate this process.\n")
                    print(f"Phone Number: {num}\n")
                    print(f"Bundle: {selected["name"]}\n")
                    print(f"Amount: ₦{selected["price"]}\n")
                    print("""
                        A.PAY
                        B.CANCEL
                        """)
                    choice1 = input("Enter your choice (A/B): ").upper()
                    if choice1 == "A":
                        while attempt < 3:
                            data_pin = input("Enter Your 4-digit pin: ")
                            if data_pin == constant.pin:
                                print("PIN VERIFIED SUCCESSFULLY")
                                print("Processing......")
                                time.sleep(5)
                                print("==============================================================")
                                print(f"You have successfully purchased {selected["name"]} Bundle valid for {selected["validity"]}")
                                print("THANK YOU FOR BANKING WITH SAM.")
                                print("==============================================================")
                                user = False
                                break
                            else:
                                print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                                attempt += 1
                                continue
                        else:
                            print("You have used all your attempt, Kindly reset your pin.")
                            break

                    else:
                        print("THANKS FOR BANKING WITH SAM")
                        app.main()


                else:
                    print("Invalid Selection.")
            elif operator == "C":
                print("Available Data Bundles: \n")
                for key,value in plans.items():
                    # print(key, value)
                    print(f"{key}. {value["name"]} ---> ₦{value["price"]}")


                choice = input("Select your data bundle from the list below (A-J) :").upper()
                selected = plans.get(choice)
                if selected:
                    print("===============================================")
                    print(f"You selected {selected["name"]}")
                    print(f"Price: ₦{selected["price"]}")
                    print(f"Validity: {selected["validity"]}")
                    print("===============================================\n")

                    print("If this is okay, respond with PAY or respond with CANCEL to terminate this process.\n")
                    print(f"Phone Number: {num}\n")
                    print(f"Bundle: {selected["name"]}\n")
                    print(f"Amount: ₦{selected["price"]}\n")
                    print("""
                        A.PAY
                        B.CANCEL
                        """)
                    choice1 = input("Enter your choice (A/B): ").upper()
                    if choice1 == "A":
                        while attempt < 3:
                            data_pin = input("Enter Your 4-digit pin: ")
                            if data_pin == constant.pin:
                                print("PIN VERIFIED SUCCESSFULLY")
                                print("Processing......")
                                time.sleep(5)
                                print("==============================================================")
                                print(f"You have successfully purchased {selected["name"]} Bundle valid for {selected["validity"]}")
                                print("THANK YOU FOR BANKING WITH SAM.")
                                print("==============================================================")
                                user = False
                                break
                            else:
                                print(f"You have entered an Invalid Pin, You have {3-attempt} remaining")
                                attempt += 1
                                continue
                        else:
                            print("You have used all your attempt, Kindly reset your pin.")
                            break

                    else:
                        print("THANKS FOR BANKING WITH SAM")
                        app.main()


                else:
                    print("Invalid Selection.")
            else:
                print("Invalid Input")
                
            
        
        