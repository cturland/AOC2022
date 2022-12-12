dataStream = []
monkeys = {}

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

    for i in range(0, len(dataStream), 7):
        monkeyName = int(dataStream[i].split(" ")[1][0:-1])

        # Items
        colon = dataStream[i + 1].index(":")
        monkey = {"items": dataStream[i + 1][colon + 2:].split(", ")}

        # Operation
        old = dataStream[i + 2].index("old")
        monkey["operation"] = dataStream[i + 2][old + 4:].split(" ")

        # Test
        by = dataStream[i + 3].index("by")
        monkey['test'] = dataStream[i + 3][by + 3:]

        # True
        end = dataStream[i + 4].index("monkey")
        monkey["true"] = dataStream[i + 4][end + 7]

        # False
        end = dataStream[i + 5].index("monkey")
        monkey["false"] = dataStream[i + 5][end + 7]

        # Inspection count
        monkey["inspection"] = 0

        monkeys[monkeyName] = monkey


def star_1():

    for r in range(20):
        for i in range(len(monkeys)):
            print("Monkey", i)
            for j in range(len(monkeys[i]["items"])):
                item = monkeys[i]["items"].pop(0)
                monkeys[i]["inspection"] += 1

                print("\tMonkey inspects an item with a worry level of", item)
                if monkeys[i]["operation"][0] == "+":
                    if monkeys[i]["operation"][1] != "old":
                        worry = int(item) + int(monkeys[i]["operation"][1])
                        print("\t\tWorry level increases by", monkeys[i]["operation"][1], "to", worry)
                    else:
                        worry = int(item) + int(item)
                elif monkeys[i]["operation"][0] == "*":
                    if monkeys[i]["operation"][1] != "old":
                        worry = int(item) * int(monkeys[i]["operation"][1])
                        print("\t\tWorry level is multiplied by", monkeys[i]["operation"][1], "to", worry)
                    else:
                        worry = int(item) * int(item)

                worry = worry // 3
                print("\t\tMonkey gets bored with item. Worry level is divided by 3 to", worry)

                if worry % int(monkeys[i]["test"]) == 0:
                    print("\t\tCurrent worry level is divisible by", monkeys[i]["test"])
                    monkeys[int(monkeys[i]["true"])]["items"].append(worry)
                    print("\t\tItem with worry level", worry, "is thrown to monkey", monkeys[i]["true"])
                else:
                    print("\t\tCurrent worry level is not divisible by", monkeys[i]["test"])
                    monkeys[int(monkeys[i]["false"])]["items"].append(worry)
                    print("\t\tItem with worry level", worry, "is thrown to monkey", monkeys[i]["false"])

                #monkeys[i]["items"].remove(item)
        currently_holding()


def star_2():

    mod = calculate_mod()

    for r in range(10000):
        for i in range(len(monkeys)):
            # print("Monkey", i)
            for j in range(len(monkeys[i]["items"])):
                item = monkeys[i]["items"].pop(0)
                monkeys[i]["inspection"] += 1

                # print("\tMonkey inspects an item with a worry level of", item)
                if monkeys[i]["operation"][0] == "+":
                    if monkeys[i]["operation"][1] != "old":
                        worry = int(item) + int(monkeys[i]["operation"][1])
                        # print("\t\tWorry level increases by", monkeys[i]["operation"][1], "to", worry)
                    else:
                        worry = int(item) + int(item)
                elif monkeys[i]["operation"][0] == "*":
                    if monkeys[i]["operation"][1] != "old":
                        worry = int(item) * int(monkeys[i]["operation"][1])
                        # print("\t\tWorry level is multiplied by", monkeys[i]["operation"][1], "to", worry)
                    else:
                        worry = int(item) * int(item)

                worry %= mod
                if worry % int(monkeys[i]["test"]) == 0:
                    # print("\t\tCurrent worry level is divisible by", monkeys[i]["test"])
                    monkeys[int(monkeys[i]["true"])]["items"].append(worry)
                    # print("\t\tItem with worry level", worry, "is thrown to monkey", monkeys[i]["true"])
                else:
                    # print("\t\tCurrent worry level is not divisible by", monkeys[i]["test"])
                    monkeys[int(monkeys[i]["false"])]["items"].append(worry)
                    # print("\t\tItem with worry level", worry, "is thrown to monkey", monkeys[i]["false"])

                #monkeys[i]["items"].remove(item)
        if r + 1 in [1, 20] or (r + 1) % 1000 == 0:
            currently_inspected(r + 1)


def currently_holding():
    for i in range(len(monkeys)):
        print("Monkey", i, ":", monkeys[i]["items"], "inspected", monkeys[i]["inspection"])


def currently_inspected(rounds):
    print("== After round", rounds, "==")
    for i in range(len(monkeys)):
        print("Monkey", i, "inspected items", monkeys[i]["inspection"], "times.")
    print()

def calculate_mod():
    mod = 1
    for i in range(len(monkeys)):
        mod *= int(monkeys[i]["test"])
    return mod


parse_data()
star_2()