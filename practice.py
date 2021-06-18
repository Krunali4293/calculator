print("Welcom to the worlds best calculator")
print ("The options for math operations are:")
print("+ for addition")
print("- for substraction")
print("* for multiplication ")
print(" / for division")
print( "** for power")
print(" % for module")
def cal():
        user=input("Enter your choice from (+,-,*,/,**,%)=")
        user1=input("Enter the first number:")
        user2=input("Enter the secont number:")
        user1=int(user1)
        user2=int(user2)
        if user=="+":
                add=user1+user2
                result=add
        elif user=="-":
                sub=user1-user2
                result = sub
        elif user=="*":
                mul=user1*user2
                result = mul
        elif user=="/":
                divi=user1/user2
                result = divi
        elif user == "**":
                pow = user1 ** user2
                result = pow
        elif user=="%":
                mod=user1%user2
                result = mod
        else:
                print("Wrong Option Selected")
        print("The result is:",result)
        user4=input("Do you want to use again it(y/n):")
        print(input("Press the Enter"))
        y = "yes"
        n = "no"
        if user4=="y":
                return cal()
        else:
                print("Thank you for using this Calculator")
cal()

