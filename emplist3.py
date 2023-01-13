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


'''def get_employee_pin_list(employee_list):
    emp_pin_list = []
    for emp in employee_list:
        emp_pin_list.append({"name": emp["name"]})
        emp_pin_list[employee_list.index(emp)][addresskey] = []
        for address in emp["address"]:
            emp_pin_list[employee_list.index(emp)][addresskey].append(address[key])
    return(emp_pin_list)

func_list = get_employee_pin_list(employee_list,address)
print(func_list)'''