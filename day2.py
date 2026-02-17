# stu_type=str(input("ENTER STUDENT TYPE:"))
# if stu_type=="msds":
#     tution_fee=float(input("enter tution fee:"))
#     bus_fee=float(input("enter bus fee:"))
#     print("THE FEES TO BE PAID BY THE STUDENT IS",tution_fee+bus_fee)
# elif stu_type=="msh":
#     tution_fee=float(input("enter tution fee:"))
#     hostel_fee=float(input("enter hostel fee:"))
#     print("THE FEES TO BE PAID BY THE STUDENT IS",tution_fee+hostel_fee)
# elif stu_type=="mgsds":
#     tution_fee=float(input("enter management tution fee:"))
#     bus_fee=float(input("enter bus fee:"))
#     print("THE FEES TO BE PAID BY THE STUDENT IS",tution_fee+bus_fee)
# elif stu_type=="mgsh":
#     tution_fee=float(input("enter management tution fee:"))
#     hostel_fee=float(input("enter hostel fee:"))
#     print("THE FEES TO BE PAID BY THE STUDENT IS",tution_fee+hostel_fee)
# else:
#     print("invalid amount")




# account_balance=50000
# withdrawal_limit=10000
# withdrawal_amount=int(input("ENTER AMOUNT:"))
# if withdrawal_amount>account_balance:
#     print("INSUFFICIENT BALANCE")
# elif withdrawal_amount>withdrawal_limit:
#     print("WITHDRAWAL LIMIT REACHED")
# else:
#     print("COLLECT YOUR CASH")



# account_balance=100000
# correct_pin=1803
# pin=int(input("ENTER YOUR PIN:"))
# if pin==correct_pin:
#     print("CORRECT PIN")
# elif pin!=correct_pin:
#     print("WRONG PIN")
# amount=int(input("ENTER AMOUNT:"))
# remaining_balance=account_balance-amount
# if amount>0 and amount<=account_balance:
#     print("WITHDRAWAL success")
#     print("REMAINING BALANCE:",remaining_balance)
# elif amount>account_balance:
#     print("INSUFFICIENT BALANCE")
# elif amount<0:
#     print("INVALID AMOUNT")




# Age = int(input("Enter your Age: "))
# Show_Time = input("Enter Your Show Time (Morning/Evening): ")
# Morning_Discount = 50
# Child_Ticket = 150
# Adult_Ticket = 250
# Senior_Ticket = 200
# if Age < 5:
#     print("Free Entry")
# elif 5 <= Age <= 17:
#     if Show_Time.capitalize() == "Morning":
#         price = Child_Ticket - Morning_Discount
#     else:
#         price = Child_Ticket
#     print("Your Child Ticket is RS.", price)
# elif 18 <= Age <= 59:
#     if Show_Time.capitalize()== "Morning":
#         price = Adult_Ticket - Morning_Discount
#     else:
#         price = Adult_Ticket
#     print("Your Adult Ticket is RS.", price)
# elif Age >= 60:
#     if Show_Time.capitalize()== "Morning":
#         price = Senior_Ticket*0.3- Morning_Discount
#     else:
#         price = Senior_Ticket*0.3
#     print("Your Senior Ticket is RS.", price)


# loop 
# sum=0
# for i in range(1,100,2):
#     print(i)
#     sum=i+sum
# print(sum)



# sum=0
# for i in range(2,100,2):
#     print(i)
#     sum=i+sum
# print(sum)



# sum=5
# for i in range(1,11):
#     print("sum,x,i,="(sum*i))



# for i in range(1,6):
#     print("*"*i)



# numbers=[5,15,25]
# total=0
# for num in numbers:
#     total += num
# print("average:",total/len(numbers))


# rows=5
# for i in range(rows,0,-1):
#     print("*"*i)


# sum=5
# for i in range(1,11):
#     print()



# while loop
# sum=0
# i=1
# while i < 100:
#     print(i)
#     sum=sum+i
#     i=i+2
# print(sum)





# total_seats = 10 
# current_seat = 1
# while current_seat <= total_seats:
#     name = input("Enter passenger name: ")
#     print(f"Seat {current_seat} booked for {name}\n")
#     current_seat += 1
# print("All seats are booked!")



