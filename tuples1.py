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






