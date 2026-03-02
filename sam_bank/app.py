"""Application entrypoint"""
from . import banking
from . import balance
from . import transfer
from . import data


def main():
    while True:
        print("==== Welcome to SAM  Chatbanking =====")
        input("press enter to continue: ")
        print("HEllO,\nHow may i assist you today? ")

        print("""
                A. Check Balance
                B. Account Opening
                C. Airtime Topup
                D. Send Money
                E. Buy Data
                F. Find SAM on FB and IG
        """)
        choice = input("Enter your choice (A-M): ").upper()
        if choice == "A":
            balance.check_balance()
        elif choice == "B":
            banking.account_opening()
        elif choice == "C":
            banking.airtime()
        elif choice == "D":
            transfer.send_money()
        elif choice == "E":
            data.user()
        elif choice == "F":
            balance.social()
        

        replay = input("Did you wish to perform a new operation? (y/n): ").lower()
        if replay != "y":
            break


if __name__ == "__main__":
    main()
