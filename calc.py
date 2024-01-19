operator = input("Wybierz operator: (+ - * /): ")
num1 = float(input("Pierwszy cyfra: "))
num2 = float(input("Druga cyfra: "))

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
    print(f"{operator} nie ma takiego operatora")
