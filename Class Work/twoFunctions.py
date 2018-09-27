num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))

def addNums(num1, num2):
    sum = num1 + num2
    return sum

def subNums(num1, num2):
    diff = num1 - num2
    return diff

def multNums(num1, num2):
    mult = num1 * num2
    return mult

def divNums(num1, num2):
    div = round(num1 / num2, 2)
    return div

def modNums(num1, num2):
    mod = num1 % num2
    return mod

print(addNums(num1, num2))

print(subNums(num1, num2))

print(multNums(num1, num2))

print(divNums(num1, num2))

print(modNums(num1, num2))