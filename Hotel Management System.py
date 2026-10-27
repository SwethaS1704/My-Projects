print("Hotel Dazzling Planet welcomes you!!")
print()
#providing users choice to choose from
print("What do you prefer doing here?")
print("If you prefer to book rooms for stay ,please enter 1")
print("If you prefer to book for meal,please enter 2")
b=input("please enter your preference:")
print()
#if the user prefers hotel
if b=='1':
    a=input("Enter your name:")
    name=a.capitalize()          
    z=int(input("Enter your phone number:"))
    q=input("Enter you address:")
    AD=q.title()                 
    print()
    w=input("Enter your city /town:")
    s=input("Enter your nationality:")
    x=input("Enter your vehicle registration number")
    print()
    e=input("Enter the date of arrival(DD MM YYYY):")
    p= e.split( )
    datea='/'.join(p)             
    print()
    d=int(input("Enter the number of days of stay:"))
    c=input("Enter the time of check in time:")
    r=input("Enter the date of departure (DD MM YYYY):")
    l=r.split( )
    dated='/'.join(l)             
    print()
    print("do you want complimentary Breakfast?:")
    f=input("yes or no :")
    print()
    if f=='yes':
         y=input("Do you prefer dine in or take out:")
    h=["1.DELUXE DOUBLE Bed Non A/C","2.DELUXE DOUBLE Bed A/C","3.DELUXE Four Bed non A/C","4.DELUXE Four Bed  A/C"]
    for n in (h) :
        print(n)
    v=input("which room do you prefer? ")
    amt=0
    if v=='1':
        amt=2000
    elif v=='2':
        amt=2500
    elif v=='3':
        amt=4000    
    elif v=='4':
        amt=4500
    else:
        print("Invalid")
    if f=='yes':
        t=(amt+500)*d
    else:
        t=amt*d
    
    print()
    #LIST MANIPULATION
     print("Rooms available: (101 - 150)(201 - 250)")
    g=eval(input("enter the preferred room numbers:"))
    l=[]
    l.extend(list(g))                                         
    print(l)
    gst=(t*(0.15)+t)*len(l)
    print()
    print("""
                               HOTEL BILL
--------------------------------------------------------------------------------------------------------
    """)
    print("Hotel Name: DAZZLING PLANET")
    print("Email ID: Dazzlingplanet@gmail.com")
    print("Phone No: +917733631845")
    print("""
--------------------------------------------------------------------------------------------------------
    """)
    print("BILLING TO:")
    print()
    print()
    print("Name:",name,end='')
    print("                                                 Phone No:",z)
    print()
    print("Address:",q)
    print()
    print("Date of Arrival:",datea,end='')
    print("                                          Time:",c)
    print()
    print("Date of Departure:",dated,end='')
    print("                                       Room No:",g)
    print("""
-------------------------------------------------------------------------------------------------------
     """)
    if v=='1'and f=='yes':
        print("""
            ----------------------------------------------------------------------------------------------------
            ROOM TYPE :                              BREAKFAST FEE:         AMOUNT:
            1. DELUXE DELUXE DOUBLE Bed Non A/C          500                2000+500
            ----------------------------------------------------------------------------------------------------
            Amount      =     2500
            Gst 15%     =      375
                        ---------------------------------

            Total       =   """,'Rs.', gst,"""
                        --------------------------------
                        
            """)
    elif v=='1' and f=='no':
        print("""
            --------------------------------------------------------------------------------------------
            ROOM TYPE :                              BREAKFAST FEE:         AMOUNT:
            1. DELUXE DELUXE DOUBLE Bed Non A/C          0                  2000
            -------------------------------------------------------------------------------------------
            Amount      =     2000
            Gst 15%     =      300
                                  ---------------------

            Total       =   """,' Rs.',gst, """
                        -------------------------
          """)
    elif v=='2'and f=='yes':
        print("""
            ----------------------------------------------------------------------------------------------
            ROOM TYPE :                              BREAKFAST FEE:         AMOUNT:
            1. DELUXE DELUXE DOUBLE Bed  A/C             500                2500+500
            ----------------------------------------------------------------------------------------------
            Amount      =     3000
            Gst 15%     =      450
                        ---------------------------------

            Total       =   """,' Rs.',gst, """  
                        ---------------------------------
            """)
    elif v=='2' and f=='no':
        print("""
            --------------------------------------------------------------------------------------------
            ROOM TYPE :                              BREAKFAST FEE:         AMOUNT:
            1. DELUXE DELUXE DOUBLE Bed  A/C             0                  2500
            --------------------------------------------------------------------------------------------
            Amount      =     2500
            Gst 15%     =      375
                        ------------------------------

            Total       =  """,' Rs.',gst, """    
                        ------------------------------
            """)
    elif v=='3' and f=='yes':
        print("""
            -----------------------------------------------------------------------------------------------
            ROOM TYPE :                              BREAKFAST FEE:         AMOUNT:
            1. DELUXE DELUXE FOUR Bed Non A/C             500               4000+500
            -----------------------------------------------------------------------------------------------
            Amount      =     4500
            Gst 15%     =      600
                        ------------------------------

            Total       =    """,' Rs.',gst, """  
                        --------------------------------
            """)
    elif v=='3' and f=='no':
        print("""
            ---------------------------------------------------------------------------------------------
            ROOM TYPE :                              BREAKFAST FEE:         AMOUNT:
            1. DELUXE DELUXE FOUR Bed Non A/C             0                 4000
            --------------------------------------------------------------------------------------------
            Amount      =     4000
            Gst 15%     =      200
                        -------------------------------

            Total       =  """,' Rs.',gst, """  
                        --------------------------------
            """)
    elif v=='4' and f=='yes':
        print("""
            -------------------------------------------------------------------------------------------------
            ROOM TYPE :                              BREAKFAST FEE:         AMOUNT:
            1. DELUXE DELUXE FOUR Bed  A/C               500                4500+500
            -----------------------------------------------------------------------------------------------
            Amount      =     5000
            Gst 15%     =      750
                        ------------------------------

            Total       =  """,' Rs.',gst, """  
                        -------------------------------
            """)
    else:
        print("""
            -------------------------------------------------------------------------------------------
            ROOM TYPE :                              BREAKFAST FEE:         AMOUNT:
            1. DELUXE DELUXE FOUR Bed  A/C               0                  4500
            -------------------------------------------------------------------------------------------
            Amount      =     4500
            Gst 15%     =      675
                        ---------------------------------

            GRAND Total  =   """ ,gst,"""
                        ---------------------------------
            """)
    print(" GRAND TOTAL:",gst)
    print("""
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                          THANK YOU

                                        Visit Again !

   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       """)
    print("Your reservation details are confirmed .")
    print("Dear,",a,"Thank you for choosing Hotel DAZZLING PLANET for your upcoming stay.”)
   print(“We're thrilled to host you and are preparing to make your visit memorable.")

elif b=='2':
    print()
    print("Restaurant welcomes you!! Choose your choice from below:")
    print("""
    ---------------FOOD MENU----------------------------------
    
            1.Vegetarian Combo --> Rs.500
            2.Non vegetaraian Combo--> Rs.700
            3.Vegetarian & Non vegetarian Combo-->Rs.900

    --------------ORDER FOOD FROM ABOVE------------------------
    
            """)
    ch=input("Enter your choice (1,2,3):")
    print("""
    -------------QUANTITY--------------
            a.small  --> 100
            b.medium  --> 150
            c.large   --> 200

   -----------ORDER FROM ABOVE---------
            """)
    quan=input("Enter how much quantity(a,b,c):")
    atm=0
    if ch=='1':
        if quan=='a':
            atm=500+100
            print("""
            ----------------------BILL-------------------------
            1. Vegetarian Combo              500+100 = 600
            ---------------------------------------------------
            TOTAL BILL =     600
            Gst 5%     =      30
                        -----------------

        Grand Total    =    Rs.630
                        ----------------
                        
            """)

        elif quan=='b':
            atm=500+150
            print("""
            ----------------------BILL-------------------------
            1. Vegetarian Combo              500+150 = 650
            ---------------------------------------------------
            TOTAL BILL =     650
            Gst 5%     =      32.5
                        ----------------- 

        Grand Total    =    Rs.682.5
                        ----------------
                        
            """)
            
        else:
            atm=500+200
            print("""
            ----------------------BILL-------------------------
            1. Vegetarian Combo              500+200 = 700
            ---------------------------------------------------
            TOTAL BILL =     700
            Gst 5%     =      35
                        -----------------

        Grand Total    =    Rs.735
                        ----------------
                        
            """)
    elif ch=='2':
        if quan=='a':
            atm=700+100
            print("""
            ----------------------BILL---------------------------------
            1. NON - Vegetarian Combo              700+100 = 800
            -----------------------------------------------------------
            TOTAL BILL =     800
            Gst 5%     =      40
                        -----------------

        Grand Total    =    Rs.840
                        ----------------
                        
            """)
        elif quan=='b':
            atm=700+150
            print("""
            ----------------------BILL---------------------------------
            1. NON - Vegetarian Combo              700+150 = 850
            -----------------------------------------------------------
            TOTAL BILL =     850
            Gst 5%     =      42.5
                        -----------------

        Grand Total    =    Rs.892.5
                        ----------------
                        
            """)
            
        else:
            atm=700+200
            print("""
            ----------------------BILL---------------------------------
            1. NON - Vegetarian Combo              700+200 = 900
            -----------------------------------------------------------
            TOTAL BILL =     900
            Gst 5%     =      45
                        -----------------

        Grand Total    =    Rs.945
                        ----------------
                        
            """)
    else:
        if quan=='a':
            atm=900+100
            print("""
            ----------------------BILL--------------------------------------------
            1. Vegetarian & NON - vegetarian Combo              900+100 = 1000
            ----------------------------------------------------------------------
            TOTAL BILL =     1000
            Gst 5%     =       50
                        -----------------

        Grand Total    =    Rs.1050
                        ----------------
                        
            """)
        elif quan=='b':
            atm=900+150
            print("""
            ----------------------BILL--------------------------------------------
            1. Vegetarian & NON - vegetarian Combo              900+150 = 1050
            ----------------------------------------------------------------------
            TOTAL BILL =     1050
            Gst 5%     =       52.5
                        -----------------

        Grand Total    =    Rs.1102.5
                        ----------------
                        
            """)

        else:
            atm=900+200
            print("""
            ----------------------BILL--------------------------------------------
            1. Vegetarian & NON - vegetarian Combo              900+200 = 1100
            ----------------------------------------------------------------------
            TOTAL BILL =     1100
            Gst 5%     =       55
                        -----------------

        Grand Total    =    Rs.1155
                        ----------------
                        
            """)
    
    print("""
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                          THANK YOU

                                        Visit Again !
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        """)
