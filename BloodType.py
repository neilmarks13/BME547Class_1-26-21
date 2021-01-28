def interface():
    print("Blood Test Analysis:")
    while 1:
        print("\nOptions")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - quit")
        choice = input("Enter an option: ")
        if choice == "1":
            hdl_driver();
        if choice == "2":
            ldl_driver();
        if choice == "9":
            return
def hdl_driver():
    data = input_hdl()
    result = analyze_hdl(data)
    output_hdl(result)
    return

def input_hdl():
    data_in = input("Enter HDL data: ")
    return data_in

def analyze_hdl(data):
    data = int(data)
    if data>=60:
        return "Normal"
    elif data>=40:
        return "Borderline Low"
    else:
        return "Low"

def output_hdl(value):
    print("HDL is {}".format(value))
    return

def ldl_driver():
    data = input_ldl()
    result = analyze_ldl(data)
    output_ldl(result)
    return

def input_ldl():
    data_in = input("Enter LDL data: ")
    return data_in

def analyze_ldl(data):
    data = int(data)
    if data<130:
        return "Normal"
    elif data<160:
        return "Borderline High"
    elif data<190:
        return "High"
    else:
        return "Very High"

def output_ldl(value):
    print("LDL is {}".format(value))
    return

interface()
# hdl_driver()