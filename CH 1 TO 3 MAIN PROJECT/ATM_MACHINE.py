#ATM MACHINE CREATE USING  VARIABLES, LOOP , IF-ELIF-ELSE CONDITION STATEMENT


balance = float(input("Enter Balance :-"))              # ENTER BALANCE

while True:                                             # WHENEVER CONDITION NOT FALSE A LOOP WILL RUN

    print("\n====== ATM Menu ======")                   # ATM MENU TO CHOICE A FUNCTIONS
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = (input("Enter Your Choice(1-4) :-"))       # ENTER CHOICE NUMBER TO PERFORM SPECIFIC TASK

    if choice == '1':                                   # TO CHECK BALANCE
        print(f"💰 Your Balance is ₹{balance}")

    elif choice == '2':                                  # TO DEPOSIT AMOUNT
         amount = float(input("Enter Amount To deposit - ₹"))
         if amount > 0:
             balance += amount
             print(f"✅ ₹{amount} deposited successfully.")
         else:
             print("❌ Enter a Valid amount.")

    elif choice == '3':                                    # TO WITHDRAW MONEY
        withdraw = float(input("Enter Withdraw Money :- ₹"))
        if 0 < withdraw <= balance:
            balance -= withdraw
            print(f"✅ ₹{withdraw} Withdrawal Successfully")
        else:
            print("❌ Insufficient  Balance or invalid amount ")

    elif choice == '4':                                     # EXIT THE ATM USING BREAK KEYWORD
        print("Thankyou for using the ATM , VISIT AGAIN")
        break                                               # BREAK KEYWORD STOP THE LOOP AND PROGRAM AFTER ARCHIVE TASK

    else:
        print("❌ Invalid choice , please try again")       # IF MENU DOSEN'T MATCH WITH CONDITION EXECUTE ELSE STATEMENT