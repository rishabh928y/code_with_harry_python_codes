# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
import time
str = input('Enter your name:')
hours = int(time.strftime('%H'))
if(hours>=0 and hours<=11):
    print("Hello ",str.capitalize(),",Good Morning")
elif(hours>=12 and hours<17):
    print("Hello ",str.capitalize(),",Good Afternoon ")
else:
    print("Hello ",str.capitalize(),",Good Evening ")        

 