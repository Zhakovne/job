with open('number.txt') as f:
    for i, line in enumerate(f):
        if i == 3:
            print(line)