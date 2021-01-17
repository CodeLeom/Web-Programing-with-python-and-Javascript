name = input("enter your name: ")
print("hello, " + name)

#conditonal statements 

n = int(input(f"{name}, kindly enter a number: "))
if n > 0:
    print(f"{n} is a positive number")

elif n < 0: 
    print(f"{n} is a negative number")

else:
    print ("your input is zero")

#lists

stores = ["Mabruur", "Zallacks", "Goddons"]

stores.append("Kaakaki")

print(stores)

stores.sort()

print(stores)