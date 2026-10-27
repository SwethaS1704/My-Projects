
print('*******************************************************')
print("🌴✈️  WELCOME TO KAD TRAVELS  ✈️🌴")
print("          Your Trusted Travel Partner")
print("----------------------------------------------------\n")




def login(email, password):
    b = email.partition('@')
    if 'admin' in b[0]:
        if password == 'adm123':
            return 'admin'
        else:
            print("Incorrect admin password!")
            return None

    with open("customers.txt", "a+",newline='') as f:
        
        f.seek(0)
        for line in f:
            line=line.strip()
            if not line:
                continue    
            
            e, p = line.strip().split(",")
            if e == email:
                if p == password:
                    return 'customer'
                else:
                    print("Wrong password!")
                    return None

        f.write(email + "," + password + "\n")
        print("EMAIL ID Registered !")
        return 'customer'

em = input("Enter your Email Id: ")
pw = input("Enter Password: ")
person = login(em, pw)

if not person:
    print("Login failed! Check your email/password")
    
if person=='customer':
    print("Let us plan you a perfect Indian Holiday!!!!!!!!!:)")
    print("Explore Top Destinations !!!")
    print()
    tp = [
        [1, " Delhi", "         ₹5000"],
        [2, " Hyderabad", "     ₹4500"],
        [3, " Goa", "           ₹6000"],
        [4, " Cochin", "        ₹5500"],
        [5, " Mumbai", "        ₹5500"],
        [6, " Bengaluru", "     ₹5500"],
        [7, " Jaipur", "        ₹4500"],
        [8, " Shimla", "        ₹5000"],
        [9, " Ooty", "          ₹4500"],
        [10,"Mysuru", "        ₹4000"]]
    print("✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈")
        
    print('ID','PLACE','         PRICE')
    print('------------------------------')
    for City in tp:
        print(City[0],City[1],City[2])
    print("✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈")
       

    print()                                                   
    dst = int(input("Choose your dream destination!😀(Enter 1-10):"))
    import mysql.connector as sqltor
    mycon=sqltor.connect(host='localhost',user='root',passwd='jgk123',database='TOURS')
    cursor=mycon.cursor()

    print()
    if dst==1:
        city='Delhi'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=1")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations in are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])

    if dst==2:
        city='Hyderabad'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=2")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])
                
    if dst==3:
        city='Goa'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=3")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])

    if dst==4:
        city='Cochin'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=4")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])


    if dst==5:
        city='Mumbai'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=5")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])

    if dst==6:
        city='Bengaluru'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=6")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])

    if dst==7:
        city='Jaipur'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=7")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])

    if dst==8:
        city='Shimla'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=8")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])

    if dst==9:
        city='Ooty'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=9")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])

    if dst==10:
        city='Mysuru'
        cursor.execute("SELECT PLACE_ID,PLACE_NAME from places where CITY_ID=10")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("The available destinations are :",count)
        print()
        print("Here's your exciting",count,"day itinerary for",city,'!')
        i=0
        for row in data:
            i=i+1
            print('DAY',i,'→',row[1])
        print()
    print()
    print("Your adventure begins here - kindly fill in your travel details:")
    print()
            
    fname=input("Enter your full name:")
    email=input("Enter your email id:")
    if email!= em:
        print("Please enter your registered EMAIL ID:")
        email=input("Enter your email id:")
        
    ph=int(input("Enter you phone number:"))
    add=input("enter your address:")
    sdate=input("Enter the tour starting date (dd/mm/yyyy) :")
    d,m,y=tuple(sdate.split('/'))
    a=True
    while a:
        if 1<=int(d)<=31 and 1<=int(m)<=12 and len(y)==4:
            a=False
            
        else:
            print(' Date Entered is Invalid!')
            sdate=input("Enter the tour starting date (dd/mm/yyyy) :")
            d,m,y=tuple(sdate.split('/'))
    
    No_per=int(input("Enter the number of person:"))
    duration=int(input("Enter the duration of the trip :"))
    mode=input('''Enter (1/2/3/4/5) for the mode of transport:
                      1. Train
                      2. Flight
                      3. Bus
                      4. Car
                      5. Cruise :''')
    catg=input(''' Enter (1/2/3/4) for the category of the room :
                    1. Budget
                    2. Deluxe
                    3. 4-star
                    4. 5-star : ''')

        

            
    amt={'Delhi':5000,'Hyderabad':4500,'Goa':6000,'Cochin':5500,'Mumbai':5500,'Bengaluru':5500,'Jaipur':4500,'Shimla':5000,'Ooty':4500,'Mysuru':4000}
    cr={'1': 2000, '2': 3000, '3': 4000, '4': 7000}  #category of the room
    Travel={"1":"Train","2":"Flight","3":"Bus","4":"Car","5":"Cruise"}
    mot = {"1": 1200, "2": 5500, "3": 800, "4": 2500,"5": 10000} #mode of travel
    print()

    play = input("Do you want to play a game to win a discount? (yes/no): ").lower()
    import random
    discount = 0
    no = random.randint(1, 10)
    st=amt[city]*No_per+mot[mode]+ cr[catg]
    gst=st*0.05
    if play == "yes":
            print()
            print("Welcome to the 'Find the Number' game!")
            print("Guess a number between 1 and 10.")

            try:
                guess = int(input("Enter your guess: "))
                if guess == no:
                    print("🎉 Correct guess! You win a 10% discount.")
                    discount = (st+gst)*0.1
                    AMOUNT=(st+gst)-discount
                else:
                    print("❌ Wrong guess! The correct number was",no,". No discount applied.")
                    AMOUNT=st+gst
            except ValueError:
                print("Invalid input. Please enter a number.")

    else:
        AMOUNT= st+gst
     
                

        
    import random
    BId="KAD"+str(random.randint(1000,9999))

        
    bclerk = ['Abinaya', 'Diksha', 'Kanishka']
    a = bclerk[random.randint(0, 2)]

    import csv
    bookings=[BId,fname,city,Travel[mode],No_per,AMOUNT]
    all_b=[]
    all_b.append(bookings)
    fh=open("cust_det.csv",'a')
    cwriter=csv.writer(fh)
    cwriter.writerows(all_b)
    fh.close()

    print('1. BOOK NOW')
    print('2. EXIT')
    ch=int(input('Enter your choice:'))
    if ch==1:
        print('------------------------------------------------')
        print('Booking successfully registered for',fname,'!!')
        print('Destination:',city)
        print('Mode of Travel:',Travel[mode])
        print('Travellers:',No_per)
        print('Duration:',duration)
        print('------------------------------------------------')
        print('Generating your bill.....')
        print('============================================================')
        print('                  BOOKING RECEIPT')
        print('============================================================')
        print('Customer ID :',BId)
        print("Customer Name :",fname)
        print("Billing Clerk:",a)
        print("Destination :",city)
        print("Mode of Travel :",Travel[mode])
        print("Travellers :",No_per)
        print("Price per Head:₹",amt[city])
        print("--------------------------------------------------------------")
        print("Subtotal: ₹",st)
        print("GST (5%): ₹",gst)
        print('---------------------------------------------------------------')
        print('💰 Total Amount: ₹',AMOUNT)
        print('---------------------------------------------------------------')
        print()
        print('Thank you for booking with KAD TRAVELS! 🌸✨')
        print('Have a wonderful jouney! ✈')

    while True:
        if ch==2:
            break
            


elif person=='admin':
    print('1. View all Bookings')
    print('2. View Total revenue')
    print('3. Search a Booking')
    print('4. Show booking statistics')
    print('5. Delete Booking')
    print()
    op=int(input("Please enter your choice:"))
    print()
    import csv

    a=True

    while a:
        
    
    
        if op==1:
            with open("cust_det.csv",'r',newline='') as fh:
                creader=csv.reader(fh)
                print("ALL BOOKINGS:")
                for rec in creader:
                    if rec:
                        print(rec)

            a=False


        elif op==2:
            import csv
            rev = 0
            with open("cust_det.csv", 'r', newline='') as fh:
                creader = csv.reader(fh)
                for rec in creader:
                    if rec:
                        rev += float(rec[5])
            print("💰 Total revenue collected: ₹", rev)
            a=False
            
                    
                
            


        elif op==3:
            with open("cust_det.csv",'r',newline='') as fh:
                bd=input("Enter Customer ID:")
                ereader=csv.reader(fh)
                for det in ereader:
                    if det:
                        if det[0]==bd:
                            print("🔎 Booking Found:" ,det)

            a=False
            
                    


        elif op==4:
            city_c = {}
            mode_c = {}
            try:
                with open("cust_det.csv", "r") as fh:
                    ereader = csv.reader(fh)
                    for det in ereader:
                        if det:  
                            city1 = det[2]
                            mode1 = det[3]

                            if city1 in city_c:
                                city_c[city1] += 1
                            else:
                                city_c[city1] = 1

                            if mode1 in mode_c:
                                mode_c[mode1] += 1
                            else:
                                mode_c[mode1] = 1

                    mcv = max(city_c.values())
                    for c in city_c:
                        if city_c[c] == mcv:
                            most_city = c
                            break

                    mmv = max(mode_c.values())
                    for m in mode_c:
                        if mode_c[m] == mmv:
                            most_mode = m
                            break

                    print("\n")
                    print("------------------------------------------------")
                    print("KAD TRAVELS - Booking Statistics                ")
                    print("------------------------------------------------")
                    print("City          | No. of Bookings                 ")
                    print("------------------------------------------------")
                    for c in city_c:
                        print(c + " "*(14-len(c)) + "| " + str(city_c[c]))
                    print("------------------------------------------------")
                    print("Most Popular City: " + most_city)
                    print("Most Popular Mode: " + most_mode)
                    print("-------------------------------------------------\n")


                    a=False

            
            except FileNotFoundError:
                print("❌ Error: No records found!")



        elif op==5:
            import csv

            with open("cust_det.csv", "r") as f:
                data = list(csv.reader(f))

            cid = input("Enter Customer ID: ")

            found = False
            new_data = []

            for record in data:
                if len(record) == 0: 
                    continue
                if record[0] == cid:
                    found = True
                    print("Record deleted:", record)
                else:
                    new_data.append(record)

            if found:
                with open("cust_det.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerows(new_data)
                print("Done! Record successfully deleted.")
            else:
                print("Customer not found!")


            a=False


        else:

            print("INVALID CHOICE!!!")
            print()
            print('1. View all Bookings')
            print('2. View Total revenue')
            print('3. Search a Booking')
            print('4. Show booking statistics')
            print('5. Delete Booking')
            print()
            op=int(input("Please enter your choice:"))

        






            
        

        

        


        
    
    
            
        
        

    


        


