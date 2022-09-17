import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
           'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
           'elon@paypal.com', 'jessica@gmail.com']
participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
                'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org',
                'mr@robot.gov', 'eleven@yahoo.com']
recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

def call_center():
    return list(set(clients + participants) - set(recipients))

def potential_clients():
    return list(set(participants) - set(clients))

def loyalty_program():
    return list(set(clients) - set(participants))

def create_list():
    choice_list = {'call_center': call_center,
                   'potential_clients': potential_clients,
                   'loyalty_program': loyalty_program
                   }
    try:
        print(choice_list[sys.argv[1]]())
    except KeyError as e:
        print('Exception', e)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        create_list()

# call_center, potential_clients, loyalty_program