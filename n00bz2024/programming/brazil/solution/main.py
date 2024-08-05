import random, time

def solve(eggs):
    text = """abc
    """

    return sum([ord(c) for c in text])

n = 1000
start = time.time()

for _ in range(10):
    eggs = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(0, 696969))
            print(row[j], end=' ')
        eggs.append(row)
        print()

    solution = solve(eggs)
    print("optimal: " + str(solution))
    inputPath = input()
    inputAns = eggs[0][0]
    x = 0
    y = 0

    for direction in inputPath:
        match direction:
            case 'r':
                x += 1
            case 'd':
                y += 1
            case _:
                exit()

        if x == n or y == n:
            print("out of bounds")
            exit()

        inputAns += eggs[x][y]



    if inputAns < solution:
        print(inputAns)
        print("you didn't find enough eggs")
        exit()

print("tnxs for finding all my eggs")
f = open("/flag.txt.txt", "r")
print(f.read())