
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))

print("Please press\n 1 for addition\n 2 for subtraction\n 3 for multiplication\n 4 for division\n 5 for power\n 6 for floor division\n 7 to get remainder ")

choice = int(input("Please Enter Your Choice : "))

if choice==1:
    print("SUM of ",num1,"and",num2,"is : ",num1+num2)
elif choice==2:
    print("Difference of ",num1,"and",num2,"is : ",num1-num2)
elif choice==3:
    print("Product of ",num1,"and",num2,"is : ",num1*num2)
elif choice==4:
    print("Division of ",num1,"and",num2,"is : ",num1/num2)

elif choice==5:
    print("Power of ",num1,"is to",num2,"is : ",num1**num2)
elif choice==6:
    print("Floor Division of ",num1,"and",num2,"is : ",num1//num2)
elif choice==7:
    print("Remainder on Division of ",num1,"and",num2,"is : ",num1-num2)
else:
    print("Please give valid input........")
