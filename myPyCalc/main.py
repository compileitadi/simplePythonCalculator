def add(x, y):
    #adds both the values
    return x + y

def substract(x, y):
    #substracts the vale of y from x
    return x - y

def multiply(x, y):
    #multiples both values
    return x * y

def divide(x, y):
    #divides y times x
    return int(x/y)

while True:
    #infine loop for unlimited trials
    print("")
    print("=====Simple Calculatror=====")
    print("1: Add")
    print("2: Substact")
    print("3: Multiply")
    print("4: Divide")
    print("5: Quit")
    print("")

    choice = input("Enter a choice(1-5) : ")

    if choice == "5":
        #breaks out of the loop
        print("Good Bye!!!")
        break

    if choice in  ["1","2","3","4"]:

        try:
            num1  = int(input("Enter Number 1 : "))
            num2  = int(input("Enter Number 2 : "))

        except ValueError:
            print("Please Enter valid integers! ")
            continue

        if choice == "1" :
            print("Result : ", add(num1,num2))
        elif choice == "2":
            print("Result : ", substract(num1,num2))
        elif choice == "3":
            print("Result : ", multiply(num1,num2))
        elif choice  == "4":
            print("Result : ", substract(num1,num2))
    else:
        print("Invalid Choicer!!!")