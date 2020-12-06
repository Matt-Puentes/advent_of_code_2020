import re
input_file = []
with open("input", "r") as f:
    input_file = f.read()

processed_file = re.findall("([0-9]+)-([0-9]+) (.): (.*)", input_file)

print(processed_file)

def part_2():
    good_count = 0
    for line in processed_file:
        index_1 = int(line[0])
        index_2 = int(line[1])
        letter = line[2]
        passwd = line[3].strip()
        print(line)

        index1 = passwd[index_1 - 1] == letter
        index2 = passwd[index_2 - 1] == letter

        if(index1 ^ index2):
            print("bad line")
            print(index1, index2, passwd[index_1 - 1], passwd[index_2 - 1])
            good_count += 1

    print(good_count)

def part_1():
    bad_count = 0
    for line in processed_file:
        min_num = int(line[0])
        max_num = int(line[1])
        letter = line[2]
        passwd = line[3].strip()

        count = 0
        for char in passwd:
            if char == letter:
                print(char)
                print(letter)
                print("===")
                count += 1
        
        if count > max_num or count < min_num:
            print(count, max_num, min_num)
            print("bad line")
            print(line)
            bad_count += 1

    print(bad_count)
    print(len(processed_file) - bad_count)

part_2()