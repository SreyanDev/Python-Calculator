try:

    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))


    operator = input("Enter the operator (+,-,*,/) : ")

    match operator:

        case "+":

            result=a+b              #No need to assign datatype for f"The sum of {a} and {b} is {result}" like in C cuz python detect it automatically.

            print(f"The sum of {a} and {b} is {result}.")

        case "-":

            result=a-b
            print(f"The difference of {a} and {b} is {result}.")

        case "*":

            result=a*b
            print(f"The product of {a} and {b} is {result}.")

        case "/":

            if b!=0:
                result=a/b
                print(f"The division of {a} and {b} is {result}.")

            else:
                print(f"Since the value of b is 0 the answer {a}/{b} is not defined.")


        case _:
            print("Enter the correct operator (+,-,*,/).")

except Exception as e:
    print(f"{e} .\"\"Enter integer or float numbers only.\"\"")
