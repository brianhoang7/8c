class Employee:
    def __init__(self, name, ID_number, salary, email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address

    dic_employee = {}
def make_employee_dict(name, ID_number, salary, email_address):
    tally = 0
    for tally in range(len(self.name)):
        name[tally] = Employee(ID_number[tally], salary[tally],email_address[tally])
        dic_employee[ID_number[tally]] = name[tally]
        tally+=1
    return dic_employee