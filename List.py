elem = [8, 9, "Thor", "Ironman"]
print(len(elem))
print(elem[0])
print(elem[-1])

avengerlist= [ "Ironman", "capital American", "Thor", "Hulk"]
ratinglist= [10, 9, 8, 6, 7, 8]
ratedAvenger = []

for i in range(len(avengerlist)):
    ratedAvenger.append(avengerlist[i])
    ratedAvenger.append(ratinglist[i])
print(ratedAvenger)
