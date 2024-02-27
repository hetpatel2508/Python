for i in "het":
    print(i)


print("")
for i in range(5):  # for(int i=0;i<5;i++)
    print(i)


#for(int i=0;i<5;i+2)   =>  for i in range(5,0,2) = 024
#for(int i=0;i<5;i+2)   =>  for i in range(5,0,-2) = 531


print("")
for i in range(5,0,-1): #54321
    print(i)

print("")
for i in range(5,-1,-1): #543210
    print(i)


print("")
for i in range(2, 5):  # for(int i=2;i<5;i++)
    print(i)


print("")
name = ["het", "dev", "sahil", "deep", "urvish"]
for i in name:
    print("My Name is ", i)


# or

print("")
for i in ["het", "dev", "sahil", "deep", "urvish"]:
    print("My Name is ", i)


print("")
persone = {"id":1,"name":"het","email":"het@123"}
for key,value in persone.items():
    print(key," = ",value)


print("")
print("")
persone = [{"id": 1, "name": "het"}, {"id": 2, "name": "dev"}, {"id": 3, "name": "sahil"}]
for i in persone:
    print("id = ",i["id"],"  ","Name = ",i["name"])