# ratedAvengerList2D=[
#     {"Spiderman",8},
#     {"Groot",7},
#     {"Blach Widow",8}
# ]
# for i in range(0, len(ratedAvengerList2D)):
#     # print(ratedAvengerList2D[i])
#     for j in range(0, len(ratedAvengerList2D[i])):
#         print(ratedAvengerList2D[i][j])

# employee = {
#     "name": "Tony Stack",
#     "emp_id": 3,
#     "address": [
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "WB",
#             "pincode": "700107"
#         },
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "WB",
#             "pincode": "700107"

#         }
#     ]
# }
# for i in range(0, len(employee["address"])):
#     print(employee["address"][i]["pincode"])

# ratedAvengerList2D=[
#     {"Spiderman",8},
#     {"Groot",7},
#     {"Blach Widow",8}
# ]
# for elem in ratedAvengerList2D:
#     for innerElem in elem:
#         print(innerElem)

# avengeraDict = {
#     "Ironman": 10,
#     "Capital America": 9,
#     "Thor": 8
# }


employee_list= [
    {
        "name": "Tony Stack",
        "emp_id": 3,
        "address": [
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "pincode": "700107"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "pincode": "700107"
            }
        ]
    },
    {
        "name": "Steve Rogers",
        "emp_id": 6,
        "address":[
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "pincode": "700107"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "pincode": "700107"
            }
        ]
    }
]
emp_pin_list = []
for emp in employee_list:
    # print("Name: ", emp["name"])
    # print("Id: ",emp["emp_id"])
    emp_pin_list.append({"name": emp["name"]})
    print(emp_pin_list)
    # print(employee_list.index[emp])
    emp_pin_list[employee_list.index(emp)]["pincode"] = []

    for address in emp["address"]:
        print(employee_list.index(emp))

        emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
        print("pincode: ",address["pincode"])
