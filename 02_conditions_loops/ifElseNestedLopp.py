# num = int(input("enter a number "))
# if(num<0):
#     print("the number is negative ")
# elif(num>0):
#     if(num<10):
#         print("the number between 1-10")
#     elif(num>10 and num<=20):
#         print("the number is between 11-20")
#     else:
#         print("the numbwer is grater than 20 ")
# else:
#     print('the number is 0')
x=int(input("enter a numberr :"))
match x:
    case 0:
        print("the number is zero ")
    case 4:
        print("the number is 4 ")
    case _ if x!=33:
        print(x,"is not 33")
    case _ :
        print(x)                