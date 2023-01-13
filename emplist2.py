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
# emp_pin_list = []
# for emp in employee_list:
#     # print("Name: ", emp["name"])
#     # print("Id: ",emp["emp_id"])
#     emp_pin_list.append({"name": emp["name"]})
#     print(emp_pin_list)
#     # print(employee_list.index[emp])
#     emp_pin_list[employee_list.index(emp)]["pincode"] = []

#     for address in emp["address"]:
#         print(employee_list.index(emp))

#         emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
#         print("pincode: ",address["pincode"])


def get_employee_pin_list(employee_list):
    emp_pin_list = []
    for emp in employee_list:
        emp_pin_list.append({"name": emp["name"]})
        emp_pin_list[employee_list.index(emp)]["pincode"] = []
        for address in emp["address"]:
            emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
    return(emp_pin_list)
    
# print(get_employee_pin_list(employee_list))

# func_list = get_employee_pin_list(employee_list)
# print(func_list)