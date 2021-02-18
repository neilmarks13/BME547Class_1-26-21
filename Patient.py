class Patient:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

def main():
    patient1 = Patient("Joe","Mama")
    # patient1.first_name = "Joe"
    # patient1.last_name = "Mama"
    print(patient1.first_name)

if __name__ == "__main__":
    main()