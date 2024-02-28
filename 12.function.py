#without return function
def gratter(a,b):           #void gratter(int a,int b)
    if(a>b):
        print(a," is bigger")
    elif(a<b):    
        print(b," is bigger")
    else:
        print("both equal")


num1=int(input("Enter Number 1 : "))
num2=int(input("Enter Number 2 : "))
gratter(num1,num2)


#with return function
def fact(num):              #int fact(int num)
    if(num==0):
        return 1
    else:
        return num*fact(num-1)

num=int(input("Enter Number : "))

factorial = fact(num)
print("Factorial = ",factorial)