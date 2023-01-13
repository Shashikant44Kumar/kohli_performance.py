def multiply(var1, var2):
    result = var1*var2
    return result

res= multiply(5, 6)
print(res)

# lambda function
multiplyx= lambda var1, var2: var1*var2  #before : put parameter after : put operation
print(multiplyx(6,6))


temp = 56

print("value of temp outside the function ",temp)

def test():
    global temp
    temp = 9
    print("value of temp inside the function ",temp)

test()
print("value of temp after the function ",temp)

