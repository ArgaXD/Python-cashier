import time
current_time = time. time()
time_now = time.ctime(current_time)
print (time_now)

data = input("nama pelanggan: ")
print("======CAFE======")
print("Americano..........$4")
print("Caramel latte......$6")
print("milk...............$2")
print("Chocolate..........$3")

operator = input("add with (+): ")
num1 = float(input("harga item 1st: "))
num2 = float(input("harga item 2nd: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")
    


#still unfinished lmao 
 #i made this just for speedrun