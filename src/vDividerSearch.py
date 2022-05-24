from itertools import combinations


def calculateOutput(low, high, vin, error):
    vout = low / (low + high) * vin
    vout_min = low * (1 - error) / (low * (1 - error) + high * (1 + error)) * vin
    vout_max = low * (1 + error) / (low * (1 + error) + high * (1 - error)) * vin
    current = vin / (low + high) * 1000
    return vout, vout_min, vout_max, current, vout/current


def readDataBase(path):
    arr = []
    f = open(path, mode="r")
    while True:
        temp = f.readline()
        if len(temp) == 0:
            break
        else:
            arr.append(float(temp))
    f.close()
    return arr


file_opened = False

while True:

    max_input = float(input("max input voltage"))
    max_output = float(input("max output voltage"))
    percantage_error = 1.0 / 100
    max_current_consumption = 5
    min_current_consumption = 0.5


    if not file_opened:
        file_opened = True
        combinationss = list(combinations(readDataBase("myResistors.txt"), 2))

    outputList = []
    for i in range(0, len(combinationss)):
        piece = list(combinationss[i])
        low = piece[0]
        high = piece[1]
        if low > high:
            low, high = high, low

        vout, vout_min, vout_max, current, v_per_a = calculateOutput(low, high, max_input, percantage_error)
        if vout_max > max_output \
                or current > max_current_consumption \
                or current < min_current_consumption:
            vout = 0
            vout_min = 0
            vout_max = 0
            v_per_a = 0

        piece = []
        piece.append(low)
        piece.append(high)
        piece.append(vout_min)
        piece.append(vout)
        piece.append(vout_max)
        piece.append(current)
        piece.append(v_per_a)
        outputList.append(piece)

    outputList.sort(key=lambda x: x[6], reverse=False)

    row_len = 11
    for i in range(0, len(outputList)):
        sub_array = outputList[i]
        for ii in range(0, len(sub_array)):
            temp = str(round(sub_array[ii], 2))
            temp = temp + (row_len - len(temp)) * " "
            temp = temp + "|" + 3 * " "
            if ii == len(sub_array) - 1:
                print(temp, end="\n")
            else:
                print(temp, end="")
        print("-" * (15 * 7 - 3))


    print("low  R     |   ", end="")
    print("high R     |   ", end="")
    print("lower out V|   ", end="")
    print("midle out V|   ", end="")
    print("upper out V|   ", end="")
    print("current/ mA|   ", end="")
    print("V/mA       |   ", end="\n")
    print("-" * (15 * 7 - 3))
    print("\n" * 2, end="")




