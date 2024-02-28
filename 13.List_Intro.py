a = [1,2,3,4,5,6,7]
print(a)
print(type(a))
print(a[2])
print(a[-2])
print(a[len(a)-2])

#unlike other languages pyhton create array or list of more then one data type

b= [1,2,"het",3.758,True,"patel",None,[2,4,6,8]]
print(b)

#to find element in array using if
if 5 in a:
    print("Available")
else:    
    print("Not Available")


#create list from loop
    
arr1=[i+1 for i in range(5)]   # 0+1 1+1 2+1 3+1 4+1
print(arr1)

    
arr2=[i*i for i in range(5)]   # 0*0 1*1 2*2 3*3 4*4
print(arr2)

arr3=[i for i in range(10) if i%2==0]   # print even num
print(arr3)