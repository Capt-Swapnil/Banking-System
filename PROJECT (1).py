'''1. Insert Debit card
2. Choose from:
   a. Withdraw
   b. Deposit
   c. Transfer
   d. Change pin
3. Chooses to withdraw 
4. Insert amount
5. Insert pin 
6. Verifies pin
7. Verifies balance
8. Money comes out
9. Anything else want to do?
10. No
11. Show bank balance?
12. No 
13. System ends'''
#!/usr/bin/python
#cbsepython.in
import mysql.connector
mydb = mysql.connector.connect( host = "localhost", user = "root", password = "Yash@2024", database = "ATM_System")
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM data")
info1 = mycursor.fetchall()
info = list(info1)
count = 0
#print(info)
a = 0
n = 0
c= 0

# while loop checks existance of the enterd username
while True:
    user = input('\nENTER YOUR NAME AND INSERT YOUR CARD : ')
    print(user)
    #user = user.lower()
    while a <= 5:
        if user == info[a][0]:
            n = a
            c = 1
            break
        a = a+1
    if (c!=1):
            print('****************')
            print('INVALID USERNAME')
            print('****************')
    break  

# comparing pin
while count < 3:
    print('******************')
    pin = str(input('PLEASE ENTER PIN: '))
    print('******************')
    if pin.isdigit():
        pin = int(pin)
        if user == info[n][0]:
                if pin == info[n][1]:
                    break
                else:
                    count += 1
                    print('***********')
                    print('INVALID PIN')
                    print('***********')
                    print()
            
# in case of a valid pin- continuing, or exiting
if count == 3:
    print('***********************************')
    print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')
    print('-----------------------------------')
    exit()

print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print()
print('**************************')    
print('Welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
def statement():
        print('*********************************************')
        print(info[n][0], 'YOU HAVE ', info[n][2],'RUPEES ON YOUR ACCOUNT.')
        print('*********************************************')
        
def withdraw():
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************')
        if cash_out%10 != 0:
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 RUPEES NOTES')
            print('******************************************************')
        elif cash_out > info[n][2]:
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
        else:
            bal = info[n][2] - cash_out
            print('***********************************')
            print('YOUR NEW BALANCE IS: ', bal, 'RUPEES')
            print('***********************************')
            input_data = (bal,info[n][2])
            sql = "update data set ACCOUNT_BALANCE = %s where ACCOUNT_BALANCE = %s"
            mycursor.execute(sql,input_data)
            mydb.commit()
            
def lodge(): 
        print()
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
        print('*********************************************')
        print()
        if cash_in%10 != 0:
            print('****************************************************')
            print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 RUPEES NOTES')
            print('****************************************************')
        else:
            bal = info[n][2] + cash_in
            print('****************************************')
            input_data = (bal,info[n][2])
            sql = "update data set ACCOUNT_BALANCE = %s where ACCOUNT_BALANCE = %s"
            mycursor.execute(sql,input_data)
            mydb.commit()
            print('YOUR NEW BALANCE IS: ', bal, 'RUPEES')
            print('****************************************')
            
        
        
def password():
        print('*****************************')
        new_pin = str(input('ENTER A NEW PIN: '))
        print('*****************************')
        if new_pin.isdigit() and new_pin != info[n][1] and len(new_pin) == 4:
            print('******************')
            new_pin = int(new_pin)
            new_ppin = int(input('CONFIRM NEW PIN: '))
            print('*******************')
            if new_ppin != new_pin:
                print('************')
                print('PIN MISMATCH')
                print('************')
            else:
                sql = "update data set ACCOUNT_BALANCE = %s where ACCOUNT_BALANCE = %s"
                input_data = (new_pin, info[n][1])
                mycursor.execute(sql,input_data)
                mydb.commit()
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('*************************************')
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('*************************************')
            print('-------------------------------------')
        

while True:
    print('*******************************')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
    print('*******************************')
    valid_responses = ['s', 'w', 'l', 'p', 'q']
    response = response.lower()
    if response == 's':
        statement()
    elif response == 'w':
         withdraw()
    elif response == 'l':
        lodge()
            
    elif response == 'p':
        password()
    elif response == 'q':
        exit()
        print("******THANK YOU! HAVE A NICE DAY !********")
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')
