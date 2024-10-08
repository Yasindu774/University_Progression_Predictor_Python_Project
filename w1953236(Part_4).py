# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953236
# Student Name: Yasindu Anushka Gunasekara
# Date: 12/02/2022

credit_pass = 0
credit_defer = 0
credit_fail = 0
user_id = ''
user_id_list = []


def enter_data():
    global user_id
    global credit_pass
    global credit_defer
    global credit_fail
    global user_id_list

    while True:
        user_id = input('Enter User id: ')
        if user_id not in user_id_list:
            user_id_list.append(user_id)
            try:
                credit_pass = int(input('Please enter your credits at pass: '))
                if credit_pass in range(0, 140, 20):
                    credit_defer = int(input('Please enter your credits at defer: '))
                    if credit_defer in range(0, 140, 20):
                        credit_fail = int(input('Please enter your credits at fail: '))
                        if credit_fail in range(0, 140, 20):
                            total = credit_pass + credit_defer + credit_fail
                            if total == 120:
                                break
                            else:
                                print('Total incorrect.')
                                continue
                        else:
                            print('out of range.')
                    else:
                        print('Out of range.')
                else:
                    print('Out of range.')
            except ValueError:
                print('Integer required')

        else:
            print('Please Enter Unique ID')


# credits_store_in_a_list
credit_list = [[], [], [], []]


def store_credit(a, b, c):
    global i
    global credit_list
    credit_list[i].append(a)
    credit_list[i].append(b)
    credit_list[i].append(c)


def outcomes():
    global i
    if credit_pass == 120:
        print('Progress')
        i = 0
        store_credit(credit_pass, credit_defer, credit_fail)
    elif credit_pass == 100:
        print('Progress (module trailer) ')
        i = 1
        store_credit(credit_pass, credit_defer, credit_fail)
    elif credit_pass == 80 or credit_pass == 60 or (credit_pass == 40 and credit_defer != 0):
        print('Do not Progress – module retriever ')
        i = 2
        store_credit(credit_pass, credit_defer, credit_fail)
    elif (credit_pass == 20 and credit_defer > 20) or (credit_pass == 0 and credit_defer >= 60):
        print('Do not Progress – module retriever ')
        i = 2
        store_credit(credit_pass, credit_defer, credit_fail)
    elif credit_pass == 40 or credit_pass == 20 or credit_pass == 0:
        print('Exclude ')
        i = 3
        store_credit(credit_pass, credit_defer, credit_fail)


def store_dictionary():
    chunk_size = 3
    mark_dict = {}
    r = 0
    for y in credit_list:

        for i in range(0, len(y), chunk_size):
            value = user_id_list[r]
            mark1 = f'progress - {str(y[i:i + chunk_size])[1:-1]}'
            mark2 = f'Progress (module trailer) - {str(y[i:i + chunk_size])[1:-1]}'
            mark3 = f'Module retriever - {str(y[i:i + chunk_size])[1:-1]}'
            mark4 = f'Exclude - {str(y[i:i + chunk_size])[1:-1]}'
            if y == credit_list[0]:
                mark_dict[value] = mark1
            elif y == credit_list[1]:
                mark_dict[value] = mark2
            elif y == credit_list[2]:
                mark_dict[value] = mark3
            elif y == credit_list[3]:
                mark_dict[value] = mark4

            r += 1
    print(mark_dict)


enter_data()
outcomes()
continue_quit = input('''Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results: ''')
if continue_quit == 'y':
    while continue_quit == 'y':
        enter_data()
        outcomes()
        continue_quit = input('''Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results: ''')
    if continue_quit == 'q':
        store_dictionary()

elif continue_quit == 'q':
    store_dictionary()
else:
    print('Try Again!!')