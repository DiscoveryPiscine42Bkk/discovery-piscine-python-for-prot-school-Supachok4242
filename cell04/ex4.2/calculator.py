def calculator():
    try:
        num1 = float(input("Give me the first number: "))
        num2 = float(input("Give me the second number: "))

        print("Thank you!")

        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} / {num2} = {num1 / num2}")
        print(f"{num1} * {num2} = {num1 * num2}")

    except ValueError:
        print("Invalid input. Please enter numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

if __name__ == "__main__":
    calculator()