i = 0
while (i<7):
    print(i)
    i+=1
    if i==4:
        break

else:
    print("this is else block")   

for x in range(5):
    print(f"iteration no{x} in for loop", (x+1))
else:
    print("this is else block in for loop")  
print("this is outside of for loop")