# a = 5
# b = 12
# c = "Shashi"
# print("value of the variable :",a)
# print("Type of the variable: ",type(c))


# print("Answer is: ",a+b)
# print("Answer is: ",a-b)
# print("Answer is: ",a*b)
# print("Answer is: ",a/b)

# # using for loop
# elements = []
# for i in range(10):
#     elements.append(i)
#     print(elements)

# print(elements)  

# first_name = input()
# last_name = input()
# print(first_name+" " +last_name)
# print(type(first_name))
# print(type(last_name))

# num1=int(input("enter first in number "))
# num2=int(input("enter second number "))
# print(num1 + num2)

# val = "HUNTER"
# print(type(val))
# for i in range(len(val)):
#     print(val[i], type(val[i]))

# elem = [8, 9, "Thor", "Ironman"]
# print(len(elem))
# print(elem[0])
# print(elem[-1])

# avengerlist= [ "Ironman", "capital American", "Thor", "Hulk"]
# ratinglist= [10, 9, 8, 6, 7, 8]
# ratedAvenger = []

# for i in range(len(avengerlist)):
#     ratedAvenger.append(avengerlist[i])
#     ratedAvenger.append(ratinglist[i])
# print(ratedAvenger)

# avengerlist= [ "Ironman", "capital American", "Thor", "Hulk"]
# avengerlist[3]= "Boatman"
# print(avengerlist)

# avengerDict = {
#     "ironman": 10,
#     "cap America": 9,
#     "thor": 8
# }
# print(avengerDict)
# print(type(avengerDict))

avengerDict = {
    "Ironman": [
        {"spiderman": 8},
        {"Black panther": 7}
    ],
    "Thor": [
        {"Hulk": 8},
        {"Groot": 7}
    ]


}
print(len(avengerDict))
teamIronman = avengerDict["Ironman"]
print("TEAM IRON MAN: ", teamIronman)
teamThor = avengerDict["Thor"]
print("TEAM THOR: ", teamThor)