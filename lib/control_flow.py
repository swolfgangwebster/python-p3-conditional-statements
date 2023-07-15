#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username in ["admin", "ADMIN"] and password == "12345"):
        return "Access granted"
    return "Access denied"
    pass

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    if temperature < 65:
        return "It's a little chilly out there!"
    if temperature > 85:
        return "It's too dang hot out there!"
    return "It's perfect out there!"
    pass

def fizzbuzz(num):
    # your code here
    if (num%3 == 0 and num%5==0):
        return "FizzBuzz"
    if (num%3 == 0):
        return "Fizz"
    if (num%5 == 0):
        return "Buzz"
    return num

    pass

def calculator(operation, num1, num2):
    # your code here
    if (operation == "+"):
        return num1 + num2
    if (operation == "-"):
        return num1 - num2
    if (operation == "*"):
        return num1 * num2
    if (operation == "/"):
        return num1 / num2
    print("Invalid operation!")
    return None
    pass
