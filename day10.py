dataStream = []
signal_strength = []

def parse_data():
    global dataStream
    # opening the file in read mode
    my_file = open("data.txt", "r")

    # reading the file
    data = my_file.read()

    # replacing end splitting the text
    # when newline ('\n') is seen.
    dataStream = data.split("\n")
    my_file.close()


def calculate_signal_strength(cycles, register, check_strength):
    if cycles == check_strength:
        signal_strength.append(cycles * register)
        print(check_strength, cycles, register, signal_strength)
        check_strength += 40
    return check_strength


def star_1():
    register = 1
    cycles = 0
    check_strength = 20

    for i in range(len(dataStream)):
        ins = dataStream[i].split(" ")
        #print(ins)

        if ins[0] == "noop":
            cycles += 1
            check_strength = calculate_signal_strength(cycles, register, check_strength)
        elif ins[0] == "addx":
            cycles += 1
            check_strength = calculate_signal_strength(cycles, register, check_strength)
            cycles += 1
            check_strength = calculate_signal_strength(cycles, register, check_strength)
            register += int(ins[1])


    print(sum(signal_strength))

parse_data()
star_1()


