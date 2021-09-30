pin = 1243
bal = 0
withdraw = 0 
answer = 'y'
password = 0000
trial = 3

while pin != password and trial > 0:  
    password = int(input('Please input your password:'))
    if pin != password:
        print(" Wrong pin")
        trial= trial - 1
        if trial == 0:
            print('try again later!!...')
    else:
        while answer == 'Y' or 'y':
            print('***Menu***')
            print('Balance : ' + str(bal))
            print('1. Withdraw\n2. Deposit\n3. Exit')
            select = int(input('Please input selection: '))
            if select == 1:
                print('***Withdraw***')
                # bal = int(input('Balance: '))
                print('Balance : ' + str(bal))
                withdraw = int(input('Please input withdraw amount: '))
                int(bal)
                y = bal
                bal = y - withdraw
                if bal < 0:
                    print('Invalid Transaction!!!\nRetry the Process!\n')
            elif select == 2:
                print('***Deposit***')
                dep = int(input('Please Input Deposit Amout: '))
                x = bal
                bal = x + dep
            elif select == 3:
                print('Are you sure you want end the Transaction?')
                answer = input('Go back to first page? (Y/N) : ')