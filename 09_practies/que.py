positive = 0
negative = 0
even=0
odd=0
total=0
for i in range(10):
    num = int(input("enter the value :"))
    total =total +num
    
   
    if(num>0):
        positive = positive +1
    elif(num<0):
        negative =negative +1
    
    if(num%2==0):
        even = even +1
    else:
        odd = odd+1
        
       
        
average = total/10
print("the positive number is :\n",positive)
print("the negative number is :\n",negative)
print("number of even value is :\n",even)
print("number of odd value is :\n",odd)
print("average :",average)
