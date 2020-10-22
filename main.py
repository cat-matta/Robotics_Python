'''
print("Hello")
#print(232)
#print('Hello')
print("Hello " +"23")
x=23
y="STring"
print(x)
print(y)
print("yis a ",type(y))
name="Cat"

print("Hello, {}. YOu are {}".format(name,21))
fhjfgk
'''
import random as r
import math



flo=23.45323
con=True 
co=False
#print(co)
complex_num=2+3j
#print(complex_num.imag)
#print("2^5==",2**5)
number=5
number*=2 #same as number= number*2
#print(number)
number=str(number)
#print("Hello"+number)
name="Harron"
# x=input("Please put something: ")
# try:
#     x=int(x)
#     print(x**2)
# except:
#     print("PUt a number please")

# name="catherine"
# # print(name[0])
# # print(name[3])
# # print(name[:3]) # h is not included
# # print(name[3:]) # h to the end
# # print(len(name))
# # print(name[3:7]) #not including 7
# print(name[8])
# #or
# print(name[-2])
# #name[0]="K"
# print(name)
# name+=" sucks"
# print(name)
# new_name=name[1:]
# print(new_name)
# new_name= "K" +new_name
# print(new_name)

# number=52
# other=100
# if number>other:
#     print("Horray")
# else:
#     print("Boo")
# # 12<x<42
# x=14
# if (x>12 and x<42):
#     print("AND")

# if(x>12 or x<42):
#     print("OR")


lis=[]
lis.append("2")
lis.append(12)
lis.append(True)
lis.append(3.14)
lis.append("2")
lis.append(12)
lis.append(True)
lis.append(3.14)
lis.append("2")
lis.append(12)
lis.append(True)
lis.append(3.14)
lis.append("2")
lis.append(12)
lis.append(True)
lis.append(3.14)

for item in lis:
    pass
    #print("Item is",item)

#for i in (lis):
 #   print("Countdown! ",i)

x=10
while (x>0):
    pass
    #print("Horray",x)
    x-=1

def add(n1,n2):
    #print(n1+n2)
    #sum=n1+n2
    return n1+n2

sum1=add(3,2)
#print(sum1**2)

#print(math.cos(math.pi/3))
answer=r.randint(0,10)
while(True):
    guess=input("Guess a number 0-10: ")
    try:
        guess=int(guess)
        if(answer==guess):
            print("Good job!")
            break
        else:
            print("Try again")
    except:
        print("Come on man, put a number")
print("game over")

