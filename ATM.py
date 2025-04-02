def atm_machine():
    balance=1000
    while True:
        print("\nATM machine:")
        print("1.withdraw")
        print("2.deposite")
        print("3.balance")
        print("4.exit")
        choice=int(input("enter the number for the tranctation: "))

        if choice==1:
            amount=float(input("enter the amount:"))
            if amount>balance:
                print("insufficient balance:")
            else:
                balance-=amount
                print(f"the balance is:${balance}")
        elif choice==2:
            amount=float(input("enter the amount:"))
            balance+=amount
            print(f"the total balance is:${balance}")
        elif choice==3:
            print(f"the balance in your account is:${balance}")
        elif choice==4:
            print("thank you.Exit")
            break
        else:
            print("invalid choice:")
atm_machine()
