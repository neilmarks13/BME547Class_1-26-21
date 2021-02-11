def create_database_entry(name,id_no,age):
    new_patient = [name,id_no,age, []]
    return new_patient

def find_patient(id_no,db):
    for patient in db:
        if patient[1]==id_no:
            return patient[0]
    return 'Patient ID Not Found'

def print_directory(db):
    for i,patient in enumerate(db):
        print("{}. Name: {}, id: {}, age: {} test results: {}" .format(i+1,patient[0],
        patient[1],patient[2],patient[3]))
    
def add_test_results(id_no,db,test_name,test_results):
    for patient in db:
        if patient[1] == id_no:
            patient[3].append((test_name,test_results))
    
def main():
    db = []
    db.append(create_database_entry('Joe Mama',123,56))
    db.append(create_database_entry('Ricky Bobby',87,42))
    db.append(create_database_entry('Karen',189,50))
    db.append(create_database_entry('Patrick Star',420,21))
    add_test_results(420,db,'HDL',65)
    add_test_results(420,db,'LDL',150)
    print_directory(db)
    print(find_patient(420,db))

if __name__ == "__main__":
    main()