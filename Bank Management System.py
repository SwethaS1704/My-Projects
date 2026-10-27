import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",
                     user="root",
                     passwd="Swethasrini2009",
                     database="customerdetail")
if mycon.is_connected()== False:
    print("Error connecting to mysql database")
cursor=mycon.cursor()

cursor.execute('''create database
               if not exists customerdetail''');
cursor.execute("use customerdetail");
cursor.execute("""
create table if not exists cfile(
               accountno int auto_increment primary key,
               name varchar(10),
               age int(2),
               gender char(2),
               contactno varchar(20),
               address varchar(300),
               city varchar(100),
               aadharno char(12) unique,
               cashbalance bigint default 1000
);
""")
cursor.execute('''insert ignore into cfile
               values(79796530,'Suraj',35,'M',9894678321,
               'Anna nagar','Puducherry',893287456732,100000)''')
cursor.execute('''insert ignore into cfile
               values(79796531,'Sunitha',38,'F',9894645387,
               'Salai street','Puducherry',894678534256,50000)''')
cursor.execute('''insert ignore into cfile
               values(79796532,'Arun',40,'M',9894645698,
               'Chetty street','Puducherry',894678545656,500000)''')
cursor.execute('''insert ignore into cfile
               values(79796533,'Bala',49,'M',9894645478,
               'KVN nagar','Puducherry',894678546732,300000)''')
cursor.execute('''insert ignore into cfile
               values(79796534,'Amirtha',37,'F',9894690478,
               'Sriram nagar','Puducherry',894342146732,200000)''')

cursor.execute("""
CREATE TABLE IF NOT EXISTS fdfile (
           fdid INT AUTO_INCREMENT PRIMARY KEY,
           accountno INT,
           name VARCHAR(10),
           age TINYINT,
           aadharno CHAR(12) NOT NULL,
           panno CHAR(10),
           amount BIGINT DEFAULT 1000,
           FOREIGN KEY (accountno) REFERENCES cfile(accountno)
           ON DELETE CASCADE ON UPDATE CASCADE
);
""")
cursor.execute('''insert ignore into fdfile
               values(23456,79796530,'Suraj',35,
               893287456732,2345678923,100000)''')
cursor.execute('''insert ignore into fdfile
               values(23457,79796531,'Sunitha',38,
               894678534256,2345678967,50000)''')
cursor.execute('''insert ignore into fdfile
               values(23458,79796532,'Arun',40,
               894678545656,2345678654,500000)''')

cursor.execute('''SELECT f.accountno
FROM fdfile f,cfile c
WHERE f.accountno = c.accountno;''')

print("$$$$$$$$$$$$$$$WELCOME TO IB REATIL BANK MANAGEMENT$$$$$$$$$$$$$$")
c=input("Do you want to do any changes(deposit or withdraw money) in your account(y/n):")
while c=='y':
    print("**********************************************************")
    print('1.Create account')
    print('2.Update account details')
    print('3.Delete account')
    print('4.Deposit money')
    print('5.Withdraw money')
    print('6.Fixed deposit')
    print("**********************************************************")
    ch=int(input("Enter choice to make changes(1-6):"))

    if ch==1:
        print("Enter the following details")
        a=input("Enter your name")
        b=int(input("Enter your age"))
        c=input("Enter your gender(F/M)")
        d=int(input("Enter your contact number"))
        e=input("Enter your address")
        f=input("Enter your city")
        g=int(input("Enter your aadhar number"))
        h=input("Please pay rupees 1000 for saving in your cash account(y/n)")
        sql=('''insert into cfile
            (name,age,gender,contactno,address,city,aadharno)
             values(%s,%s,%s,%s,%s,%s,%s)''')
        val=(a,b,c,d,e,f,g)
        while cursor.nextset():
            pass
        cursor.execute(sql,val)
        print("Account created successfully")
        mycon.commit()

    if ch==2:
        s=int(input("Please enter your account number:"))
        print("1.Update contact number")
        print("2.Update address")
        print("3.Update city")
        cho=int(input("Enter choice(1-3):"))
        if cho==1:
            a=int(input("Enter new contact number"))
            sql='''update cfile
            set contactno=%s
            where accountno=%s'''
            val=(a,s)
            while cursor.nextset():
                pass
            cursor.execute(sql,val)
            print("Your contact number has been updated successfully")
        if cho==2:
            b=input("Enter new address")
            sql='''update cfile
            set address=%s
            where accountno=%s'''
            val=(b,s)
            while cursor.nextset():
                pass
            cursor.execute(sql,val)
            print("Your address has been updated successfully")
        if cho==3:
            c=input("Enter new city")
            sql='''update cfile
            set city=%s
            where accountno=%s'''
            val=(c,s)
            while cursor.nextset():
                pass
            cursor.execute(sql,val)
            print("Your city has been updated successfully")
        mycon.commit()

    if ch==3:
        a=int(input("Enter your account number to be deleted"))
        sql_child = "DELETE FROM fdfile WHERE accountno=%s"
        val_child = (a,)
        while cursor.nextset():
            pass
        cursor.execute(sql_child, val_child)
        sql_parent = "DELETE FROM cfile WHERE accountno=%s"
        val_parent = (a,)
        while cursor.nextset():
            pass
        cursor.execute(sql_parent, val_parent)
        print("Account deleted successfully")
        mycon.commit()

    if ch==4:
        a=int(input("Enter your account number"))
        e=int(input("Enter amount to be deposited"))
        sql='''update cfile
        set cashbalance= cashbalance + %s
        where accountno=%s'''
        val=(e,a)
        while cursor.nextset():
            pass
        cursor.execute(sql,val)
        print("Your amount is deposited successfully")
        mycon.commit()

    if ch==5:
        a=int(input("Enter your account number"))
        e=int(input("Enter amount to be withdrawn"))
        sql='''Select cashbalance from cfile
        where accountno=%s'''
        val=(a,)
        while cursor.nextset():
            pass
        cursor.execute(sql,val)
        r=cursor.fetchone()
        if r and r[0]>=e:
            sql='''update cfile
            set cashbalance= cashbalance - %s
            where accountno=%s'''
            val=(e,a)
            while cursor.nextset():
                pass
            cursor.execute(sql,val)
            print("You will be received with your amount")
        else:
            print("Invalid cashbalance")
        mycon.commit()
        
    if ch==6:
        print('1.Deposit')
        print('2.Withdraw')
        cho=int(input("Enter choice(1 or 2):"))

        if cho==1:
            a=int(input("Enter your account number:"))
            name=input("Enter your name:")
            age=int(input("Enter age:"))
            e=int(input("Enter amount to be deposited:"))
            t=float(input("Enter time period(in years):"))
            if age<60 and age>=18:
                print("Your amount will get the interest of 6%")
            else:
                print("Your amount will get the interest of 7%")
            sql='''update fdfile
            set amount= amount + %s
            where accountno=%s'''
            val=(e,a)
            while cursor.nextset():
                pass
            cursor.execute(sql,val)
            print("Your amount is deposited successfully")
            print("You can collect your money after",t,"years")
            mycon.commit()

        if cho==2:
            a=int(input("Enter your account number:"))
            name=input("Enter your name:")
            age=int(input("Enter age:"))
            e=int(input("Enter amount to be withdrawn:"))
            sql='''update fdfile
            set amount= amount - %s
            where accountno=%s'''
            val=(e,a)
            while cursor.nextset():
                pass
            cursor.execute(sql,val)
            print("Your amount is withdrawn successfully")
            print("You can collect your money")
            mycon.commit()
    c=input("Do you want to do anything else in your account(y/n):")
print("Thank you. Have a nice day")

        








    
