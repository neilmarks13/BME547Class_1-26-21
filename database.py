def create_database_entry(name,id_no,age):
    # new_patient = [name,id_no,age, []]
    new_patient = {"name": name, "id": id_no, "age": age, "test": []}
    return new_patient

def find_patient(id_no,db):
    for patient in db:
        if patient["id"]==id_no:
            return patient[name]
    return 'Patient ID Not Found'

def print_directory(db):
    for patient in db:
        print_patient(patient)
        print()
    
def print_patient(patient):
    for key in patient:
        print("  {}: {}".format(key, patient[key]))
    
def add_test_results(id_no,db,test_name,test_results):
    for patient in db:
        if patient["id"] == id_no:
            patient["test"].append((test_name,test_results))

def is_a_minor(patient):
    if patient["age"] < 18:
        return "minor"
    else:
        return "adult"
    
def main():
    db = []
    db.append(create_database_entry('Joe Mama',123,56))
    db.append(create_database_entry('Ricky Bobby',87,42))
    db.append(create_database_entry('Karen',189,50))
    db.append(create_database_entry('Patrick Star',420,17))
    add_test_results(420,db,'HDL',65)
    add_test_results(420,db,'LDL',150)
    print_directory(db)
    print(is_a_minor(db[2]))
    print(is_a_minor(db[3]))

if __name__ == "__main__":
    main()