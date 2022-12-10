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

def draw_pixel(cycle, sprite_pos):
    crt_width = 40
    if cycle in sprite_pos:
        print("#", end="")
    else:
        print(".", end="")

    if (cycle + 1) % crt_width == 0:
        print()
        for j in range(3):
            sprite_pos[j] += 40


def star_2():
    sprite_pos = [0, 1, 2]
    crt_height = 6
    cycle = 0

    for i in range(len(dataStream)):
        ins = dataStream[i].split(" ")

        if ins[0] == "noop":
            draw_pixel(cycle, sprite_pos)
            cycle += 1
        elif ins[0] == "addx":
            draw_pixel(cycle, sprite_pos)
            cycle += 1
            draw_pixel(cycle, sprite_pos)
            for j in range(3):
                sprite_pos[j] += int(ins[1])
            cycle += 1





parse_data()
star_2()


