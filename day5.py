stacks = [[] for _ in range(9)]
instructions = []


def parse_data():
    # opening the file in read mode
    my_file = open("data.txt", "r")

    # reading the file
    data = my_file.read()

    # replacing end splitting the text
    # when newline ('\n') is seen.
    data = data.split("\n")
    my_file.close()

    stop = False
    for i in range(len(data)):
        # Parse current stacks
        if not stop:
            stack = []
            for j in range(0, len(data[i]), 4):
                # print(line[i+1], end=" ")
                if data[i][j+1] == "1":
                    stop = True
                    break
                elif data[i][j+1] != " ":
                    stacks[j // 4].append(data[i][j+1])

        # Get instructions
        if stop and len(data[i]) > 0 and data[i][0] == "m":
            full_ins = data[i].split(" ")
            # -1 on those referring to indexes
            ins = [int(full_ins[1]), int(full_ins[3]) - 1, int(full_ins[5]) - 1]
            instructions.append(ins)

    for stack in stacks:
        stack.reverse()


def star_1():
    for ins in instructions:
        for i in range(ins[0]):
            stacks[ins[2]].append(stacks[ins[1]].pop())

    print(stacks)

    for stack in stacks:
        if len(stack) > 0:
            print(stack[len(stack) - 1], end="")


def star_2():
    for ins in instructions:
        temp=[]
        for i in range(ins[0]):
            temp.append(stacks[ins[1]].pop())

        for i in range(len(temp)):
            stacks[ins[2]].append(temp.pop())

    # print(stacks)

    for stack in stacks:
        if len(stack) > 0:
            print(stack[len(stack) - 1], end="")


parse_data()
star_2()
