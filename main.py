n = int(input("Enter the range: "))

for i in range(1, n+1) :
    if i % 20 == 0 :
        print("Twist")
    elif i % 15 == 0 :
        pass
    elif i % 5 == 0 :
        print("fizz")
    elif i % 3 == 0 :
        print("buzz")
    else :
        print(i)