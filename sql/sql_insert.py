
import random
import sqlite3

def generate_random_numbers(min, max, times):
    """generates z random numbers between range x and y"""
    numbers = []
    for n in range(times):
        numbers.append(random.randint(min, max))
    return numbers


with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS numbers(numbers INT)")


    nums = generate_random_numbers(0, 100, 100)
    print(nums)
    nums = tuple(nums)
    print(nums)

    """
    for n in nums:
        n = (n,)
        c.execute("INSERT INTO numbers VALUES(?)", (n[0],))
    """
    c.executemany("INSERT INTO numbers VALUES(?)", ((n,) for n in nums))


