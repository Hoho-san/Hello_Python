#Python ATM Machine Sample Program

balance = 100000
pin = 1234
trials = 3 
answer = 'y'

while trials > 0 and answer == 'y':
    userpin = int(input('Please input your pin:'))
    if pin != userpin:
        trials-=1
        print('Wrong PIN Number, you have ' + str(trials) + ' trial/s left')
        int(trials)
        if trials == 0:
                print('You reached maximum attempt, try again later..')
    elif pin == userpin:
        print("\nWelcome to ATM Machine of ELET-2101")

        print("\n1. Balance Inquiry")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Exit")

        option = int(input("Please enter your choice: "))
        if option == 1:
            print("Balance ₱", balance)
                
        elif option == 2:
            print("Balance ₱", balance)
            withdraw = float(input("Please enter wihtdrawal amount ₱: "))
                
            if withdraw < balance:
                newbalance = (balance - withdraw)
                print("New balance after withdrawal  ₱", newbalance)
            elif withdraw > balance:
                 print("Please withdraw amount within your balance only")
            else:
                print("None withdrawal made")

        elif option == 3:
            print("Balance ₱", balance)
            deposit = float(input("Please enter deposit amount: "))
                
            if deposit > 0:
                newbalance = (balance + deposit)
                print("New balance after deposit ₱",newbalance)
            else:
                print("None deposit made")
        elif option == 4:
            print('Exiting...')
    answer = input('Make ANOTHER TRANSACTION? (Y/N) : ')