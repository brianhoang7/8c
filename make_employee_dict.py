class Employee:
    def __init__(self, name, ID_number, salary, email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address

    dic_employee = {}
def make_employee_dict(self, name, ID_number, salary, email_address):
    tally = 0
    for tally in range(len(self.name)):
        self.name[tally] = Employee(self.ID_number[tally], self.salary[tally], self.email_address[tally])
        dic_employee[self.ID_number[tally]] = self.name[tally]
        tally+=1
    return dic_employee