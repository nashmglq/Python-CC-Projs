list = [1,2,3,4,5,6,7,8]
empty = []

def addList():
    initial = 0
    for num in list:
        initial += num

    print(initial)


if __name__ == '__main__':
    addList()