correct_pin = "123"
balance = 10000
attempts = 0
maximum_attempts = 3
transactions =[]
#login functionality
while True:
    entered_pin = input('enter your pin')
    if entered_pin ==correct_pin:
        print("pin verification is successfully done!!")
        break
    else:
        attempts =attempts+1
        print("incorrectpin,attempts left:",maximum_attempts-attempts)
        if attempts>maximum_attempts:
            print("your ATM card is blocked due to limit is exceed")
            exit()
#core functionality: menu
while True:
    print("---main memu----")
    print('press 1 for for balance checking')
    print('press 2 for deposit')
    print('prees 3 for withdrawn')
    print('press 4 for for transactions(last 4 transcation)')
    print('press 5 for exist')
    choice = input('enter your choice:')
    if choice =="1":
        print('your currentbalance is :',balance)
    elif choice=='2':
        deposit_amount>0
        balance=balance+deposit_amount
        transaction.append(f'deposited is {deposit_amount}')
        if len(transactions)>5:
            transactions.pop(0)
            print("deposit is successfull,new balance is :",balance)
        else:
            print('invalid amount')
    elif choice=='3':
            withdrawnamount = int(input('enterdranamount for withdrawn:'))
            if withdrawnamount>0 and withdrawnamount<=balance:
                balance = balance-withdrawnamount
                transactions.append(f'withdrawn:{withdrawnamount}')
                if len(transactions)>5:
                    transactions.pop(0)
                print('withdrawn is successfull,new balance is :',balance)
            else:
                    print('insufficient balance or invalid amount')
    elif choice == "4":
                    print("current transactions are:")
                    if len(transactions)==0:
                        print('no transaction done upto now')
                    else:
                        for t in transactions:
                            print(t)
    elif choice=="5":
                    print('thank you for using ATM')
                    break
    else:
                        print(" invalid")
    