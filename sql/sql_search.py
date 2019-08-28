"""
Prompt the user whether they would like to perform an aggregation (AVG, MAX,
MIN, or SUM) or exit the program altogether.


min
max
sum
average
"""

import sqlite3

def menu():
    print("""Hello, dear user!
        Here are your options:
        1: Min
        2: Max
        3: Sum
        4: Average
        5: Display the data set
        6: Quit

        Please choose the option by entering a number below,
        for example: 3""")
    answer = False
    while answer != type(int) and (answer < 1 or answer > 6):
        try:
            answer = int(input('Choose wisely\n'))
            if answer > 6 or answer < 1:
                print('Value must be a number between 1 and 6. \
For example: 1')
        except ValueError:
            print('Please give a number as an answer. \
For example: 3')
    return answer

def get_data():
    c.execute("SELECT numbers FROM numbers")
    data = c.fetchall()
    nums = []
    for d in data:
        nums.append(d[0]) 
    return nums

def get_min():
    print('The smallest number in the is: ', min(nums))

def get_max():
    print('The highest number in the is: ', max(nums))

def get_sum():
    print('The sum of the data is: ', sum(nums))

def get_average():
    print('The average is: ', sum(nums) / len(nums))

def display_data():
    print('The data is as follows: \n', nums)

def action(option):
    
    if option == 1:
        get_min()
    elif option == 2:
        get_max()
    elif option == 3:
        get_sum()
    elif option == 4:
        get_average()
    elif option == 5:
        display_data()
    elif option == 6:
        exit()

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    nums = get_data()

    while True:
        option = menu()
        action(option)
        print('')


    
    

        








