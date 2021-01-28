def interface():
    print("Blood Test Analysis:")
    while 1:
        print("\nOptions")
        print("9 - quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
def hdl_driver():
    data = input_hdl()

    return

def input_hdl():
    data_in = input("Enter HDL data: ")
    return data_in

def analyze_hdl(data):
    if data>=60:
        return "Normal"
    elif data>=40:
        return "Borderline Low"
    else:
        return "Low"

interface()