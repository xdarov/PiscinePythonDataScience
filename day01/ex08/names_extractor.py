import sys


def main(email):
    filename = 'employees.tsv'
    with open(filename, 'r') as f:
        employees = f.read()
    name = parse_employees(email, employees)
    text = f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires."
    if name:
        return text


def parse_employees(email, employees):
    for employee in employees.split('\n'):
        employee = employee.split('\t')
        if len(employee)!= 3:
            continue
        if employee[2] == email:
            return employee[0]
    

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            print(main(sys.argv[1]))
        else:
            raise ValueError('Count of arg')
    except ValueError as e:
        print('Exception:', e)
   