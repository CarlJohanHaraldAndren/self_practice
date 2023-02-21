def passwords(file):
    dictionary=[]
    min_dick={}
    file=open(file)
    lines=file.readlines()
    file.close()

    for line in lines:
        dictionary.append(line.lstrip().replace("\n",""))

    for line in dictionary:
        split_lines=line.split()
        #print(split_lines)
        min_dick[split_lines[0]] = split_lines[1]

    return min_dick

print(passwords('passwords.txt'))