def collatz(currentNumber):
    if currentNumber%2 == 0: # it's even
        value = currentNumber//2
        print(value)
        return value
    else:
        value = currentNumber*3+1
        print(value)
        return value

while True:
    try:
        number = int(input("Enter a number "))
        while number != 1:
            number = collatz(number)
    except:
        print("Error was generated")