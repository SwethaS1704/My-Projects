print(".......................WELCOME TO SMART HOME!!!!!!............................")
print()
print("Here are the appliances with brand name and cost.Kindly choose the appliances you want.")
print()
mlist=["1.LED TV","2.Washing machine","3.Mixer grinder","4.AC","5.Smart phones"]
length=len(mlist)
for s in range(length):
    print(mlist[s])
print()

Cost=0
acost=0
bcost=0
ccost=0
dcost=0
ecost=0
count=0

a=str(input("Do you want to purchase:"))
list=[]
while a=='yes':
    ch=int(input("Enter choice(1 to 5):"))
    if ch==1:
        print("1.Sony 32 inch- Rs.38900")
        print("2.LG 32 inch- Rs.21900")
        print("3.Samsung 32 inch- Rs.19900")
        print("4.Vu 32 inch- Rs.25900")
        print("5.Micromax 32 inch- Rs.24900")
        ch1=int(input("Enter choice(1 to 5):"))
        if ch1==1:
            list+=["sony tv"]
            Cost=38900
        elif ch1==2:
            list+=["lg tv"]
            Cost=21900
        elif ch1==3:
            list+=["samsung tv"]
            Cost=19900
        elif ch1==4:
            list+=["vu tv"]
            Cost=25900
        elif ch1==5:
            list+=["micromax tv"]
            Cost=24900
        acost+=Cost
        count+=1
        print("Total cost=",acost)
        print()

    elif ch==2:
         print("1.IFB senator- Rs.37990")
         print("2.Bosch- Rs.58590")
         print("3.Lg - Rs.50490")
         print("4.Samsung- Rs.17990")
         print("5.Whirlpool- Rs.18990")
         ch2=int(input("Enter choice(1 to 5):"))
         if ch2==1:
             list+=["ifb washing machine"]
             Cost=37990
         elif ch2==2:
             list+=['bosch washing machine']
             Cost=58590
         elif ch2==3:
             list+=['lg washing machine']
             Cost=50490
         elif ch2==4:
             list+=['samsung washing machine']
             Cost=17990
         elif ch2==5:
             list+=['whirlpool washing machine']
             Cost=18990
         bcost+=Cost
         count+=1
         print("Total cost=",bcost)
         print()
         
    elif ch==3:
        print("1.Butterfly-RS.4999")
        print("2.Preethi-RS.13999")
        print("3.Maharaja-Rs.3999")
        print("4.Prestige-Rs.4999")
        print("5.Philips-Rs.6999")
        ch3=int(input("Enter choice(1 to 5):"))
        if ch3==1:
            list+=["butterfly mixer grinder"]
            Cost=4999
        elif ch3==2:
            list+=["preethi mixer grinder"]
            Cost=13999
        elif ch3==3:
            list+=["maharaja mixer grinder"]
            Cost=3999
        elif ch3==4:
            list+=["prestige mixer grinder"]
            Cost=4999
        elif ch3==5:
            list+=["philips mixer grinder"]
            Cost=6999
        ccost+=Cost
        count+=1
        print("total cost =",ccost)
        print()
    
    elif ch==4:
        print("1.Daikin- Rs.58490")
        print("2.Bluestar- Rs.61290")
        print("3.Carrer- Rs.67790")
        print("4.Lg- Rs.36990")
        print("5.LLOYD- Rs.59990")
        ch4=int(input("Enter choice(1 to 5):"))
        if ch4==1:
            list+=["daikin ac"]
            Cost=58490
        elif ch4==2:
            list+=["bluestar ac"]
            Cost=61290
        elif ch4==3:
            list+=["carrer ac"]
            Cost=67790
        elif ch4==4:
            list+=["lg ac"]
            Cost=36990
        elif ch4==5:
            list+=["lloyd ac"]
            Cost=59990
        dcost+=Cost
        count+=1
        print("Total cost=",dcost)
        print()
    
    elif ch==5:
        print("1.Apple- Rs.1,59,999")
        print("2.Samsung- Rs.1,09,999")
        print("3.Motorola- Rs.21,999")
        print("4.One plus-Rs.16,104")
        print("5.Redmi- Rs.13,999")
        ch5=int(input("Enter choice (1 to 5):"))
        if ch5==1:
            list+=["apple phone"]
            Cost=159999
        elif ch5==2:
            list+=["samsung phone"]
            Cost=109999
        elif ch5==3:
            list+=["motorola phone"]
            Cost=21999
        elif ch5==4:
            list+=["one plus phone"]
            Cost=16104
        elif ch5==5:
            list+=["redmi phone"]
            Cost=13999
        ecost+=Cost
        count+=1
        print("Total cost=",ecost)
        print()
    
    a=input("Do you want to purchase more?")
print("List of items purchased=",list)
print("Total no. of items purchased=",count)
    
p=acost+bcost+ccost+dcost+ecost
print("Orginal cost=",p)
q=(p*15)/100
r=p-q
print("Cost with discount=",r)
s=(r*28)/100
t=r+s
print("Total net cost=",t)
    
print("Kindly enter the following details!!!!!!!")
name=input("Enter your name:")
number=input("Enter your phone number:")
address=input("Enter your home address:")
payment=input("Enter the mode of payment(cash or card):")
date=input("Enter date to be delivered:")
time=input("Enter time to be delivered:")
print("Your products will be delivered on time!!!!!!!!!")
print("Thank you for choosing our smart home :) !!!!!!! ")
print("Have a nice day :) !!!!!!!")
print("Visit us again !!!!!!!!!!!")
        
        
        

