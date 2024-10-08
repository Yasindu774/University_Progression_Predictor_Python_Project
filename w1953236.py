# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953236
# Student Name: Yasindu Anushka Gunasekara
# Date: 12/02/2022

credit_pass = 0
credit_defer = 0
credit_fail = 0
role = input('Are you Student or Staff ? ')


# user input data & validation
def enter_data():
    global credit_pass
    global credit_defer
    global credit_fail
    global total

    while True:
        try:
            credit_pass = int(input('Please enter your credits at pass: '))
            if credit_pass in range(0,140,20):
                credit_defer = int(input('Please enter your credits at defer: '))
                if credit_defer in range(0,140,20):
                    credit_fail = int(input('Please enter your credits at fail: '))
                    if credit_fail in range(0,140,20):
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


# credits_store_in_a_list
credit_list = [[], [], [], []]


def store_credit(a, b, c):
    global i
    global credit_list
    credit_list[i].append(a)
    credit_list[i].append(b)
    credit_list[i].append(c)


# Multiple outcomes
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0


def outcomes():
    global progress_count
    global trailer_count
    global retriever_count
    global exclude_count
    global i
    if credit_pass == 120:
        print('Progress')
        progress_count += 1
        i = 0
        store_credit(credit_pass, credit_defer, credit_fail)
    elif credit_pass == 100:
        print('Progress (module trailer) ')
        trailer_count += 1
        i = 1
        store_credit(credit_pass, credit_defer, credit_fail)
    elif credit_pass == 80 or credit_pass == 60 or (credit_pass == 40 and credit_defer != 0):
        print('Do not Progress – module retriever ')
        retriever_count += 1
        i = 2
        store_credit(credit_pass, credit_defer, credit_fail)
    elif (credit_pass == 20 and credit_defer > 20) or (credit_pass == 0 and credit_defer >= 60):
        print('Do not Progress – module retriever ')
        retriever_count += 1
        i = 2
        store_credit(credit_pass, credit_defer, credit_fail)
    elif credit_pass == 40 or credit_pass == 20 or credit_pass == 0:
        print('Exclude ')
        exclude_count += 1
        i = 3
        store_credit(credit_pass, credit_defer, credit_fail)


# Horizontal Histogram
def horizontal_histogram():
    print('-------------------------------------------------------------------------------------------------')
    print('Horizontal Histogram ')
    print(f'Progress {progress_count}   : ', progress_count*' *')
    print(f'Trailer {trailer_count}    : ', trailer_count*' *')
    print(f'Retriever {retriever_count}  : ', retriever_count*' *')
    print(f'Excluded {exclude_count}   : ', exclude_count*' *')
    print('')
    print(f'{progress_count+trailer_count+retriever_count+exclude_count} outcomes in total.')
    print('-------------------------------------------------------------------------------------------------')


def data_list():
    chunk_size = 3
    for y in credit_list:
        # reference:https://www.programiz.com/python-programming/examples/list-chunks/
        for i in range(0, len(y), chunk_size):
            if y == credit_list[0]:
                # str([])[1:-1]-remove brackets reference:https://www.pythonpool.com/remove-brackets-from-list-python/
                print(f'progress - {str(y[i:i + chunk_size])[1:-1]}')
            elif y == credit_list[1]:
                print(f'Progress (module trailer) - {str(y[i:i + chunk_size])[1:-1]}')
            elif y == credit_list[2]:
                print(f'Module retriever - {str(y[i:i + chunk_size])[1:-1]}')
            elif y == credit_list[3]:
                print(f'Exclude - {str(y[i:i + chunk_size])[1:-1]} \n')


def file_save():
    f = open('output.txt', 'w')
    chunk_size = 3
    for y in credit_list:
        # reference:https://www.programiz.com/python-programming/examples/list-chunks/
        for i in range(0, len(y), chunk_size):
            if y == credit_list[0]:
                # str([])[1:-1]-remove brackets reference:https://www.pythonpool.com/remove-brackets-from-list-python/
                f.write(f'progress - {str(y[i:i + chunk_size])[1:-1]}\n')
            elif y == credit_list[1]:
                f.write(f'Progress (module trailer) - {str(y[i:i + chunk_size])[1:-1]}\n')
            elif y == credit_list[2]:
                f.write(f'Module retriever - {str(y[i:i + chunk_size])[1:-1]}\n')
            elif y == credit_list[3]:
                f.write(f'Exclude - {str(y[i:i + chunk_size])[1:-1]} \n')
    f.close()
    f = open('output.txt', 'r')
    print(f.read())


def menu():
    print('How do you want to get results?')
    print('''1. Histogram
2. List
3. Text File''')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        horizontal_histogram()
    elif choice == 2:
        data_list()
    elif choice == 3:
        file_save()
    else:
        print('Try again')


if role.upper() == 'STUDENT':
    enter_data()
    outcomes()
elif role.upper() == 'STAFF':
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
            print('-------------------------------------------------------------------------------------------------')
            menu()
    elif continue_quit == 'q':
        print('-------------------------------------------------------------------------------------------------')
        menu()
    else:
        print('Try Again!!')
else:
    print('Enter Valid Role!!!')