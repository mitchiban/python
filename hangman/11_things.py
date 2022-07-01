"""
11 Tips And Tricks To Write Better Python Code
https://www.youtube.com/watch?v=8OKTAedgFYg&t=437s
"""

# 1 - use enumerate

def old_school_without_en():
    data1 = [1, 2, -4, 4]
    for i in range(len(data1)):
        if data1[i] < 0:
            data1[i] = 0
    return print(data1)

old_school_without_en()


def with_enumerate():
    data1 = [1, 2, -4, 4]
    for idx, num in enumerate(data1):
        if num < 0:
            data1[idx] = 0
    return print(data1)

with_enumerate()


def with_enumerate():
    data1 = ['fred', 'bob', 'sam']
    for idx, name in enumerate(data1):
        if name < 0:
            data1[idx] = 0
    return print(data1)


def test_en():
    data = [1, 'harry', -4, 4, 'darren']
    
    for idx, item in enumerate(data):
        print(idx, item)

        if str(item).startswith("d") is True:
            print("starts with d")

        elif str(item).startswith("h") is True:
            print("starts with h")

        else: print("does not start with d")


test_en()


import logging

def print_vs_logging():
    logging.debug("debug info")
    logging.info("just some info")
    logging.error("uh oh :(")

def main():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s -%(messages)s'
    logging.basicConfig(level=level,format=fmt)


#print_vs_logging()