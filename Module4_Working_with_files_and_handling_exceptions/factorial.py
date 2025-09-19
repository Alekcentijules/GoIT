def factorial(num):
    if num <= 1:
        return 1
    
    print(num)
    return num * factorial(num - 1)

num = int(input("Enter the number: "))
result = factorial(num)
print(result)