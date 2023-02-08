i = int(input("Enter the number: "))
while(i<=38):
    i = int(input("Enter the number: "))
    print(i)
    
print("Done with the loop")  

count=5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else") 
    
    for i in range(12):
        if(i == 10):
            print("Skip the iteration")
            continue;     
        print("5 X", i, "=", 5 * i)
        
i=0
while True:
    print(i)
    i = i+1
    if(i%100 == 0):
        break        