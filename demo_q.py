def get_questions():
    listQ = []
    with open("qestions_file", "r") as f:
        lines = f.readlines()
        temp = []
        for i in range(len(lines) + 1):
            if i % 6 != 0 or i == 0:

                temp.append(lines[i][:-1])
            else:
                listQ.append(temp)
                temp = []
                if i + 1 < len(lines):
                    temp.append(lines[i][:-1])
    #print(listQ)
    return listQ


def get_questions_level_return(listQ,level):
    listq2 = []
    currentLevel =str(level)
    for i in range(len(listQ)):
        if listQ[i][0] == currentLevel:
            listQ[i].append(i)
            listq2.append(listQ[i])
    return listq2

def get_questions_level_new(listQ,index):
    listq2 = []
    currentLevel =listQ[index][0]
    for i in range(len(listQ)):
        if listQ[i][0] == currentLevel and i != index:
            listQ[i].append(i)
            listq2.append(listQ[i])
    return listq2

print(get_questions_level_return(get_questions(),10))
