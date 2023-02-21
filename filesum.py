def filesum(lines):
    file = open(lines)
    lines = file.readlines()
    file.close()
    new_list = list(map(int, [x.strip() for x in lines]))
    return sum(new_list)


print(filesum('numbers1.txt'))