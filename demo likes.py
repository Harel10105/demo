# Using above first method to create a
# 2D array
rows, cols = 5,5
arr = [[0]*cols]*rows
print(arr)

with open("saveLikes.txt","a+") as f:
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            f.write(str(arr[row][col])+",")

        f.write("\n")

with open("saveLikes.txt","r") as f:

    newArr = f.readlines()
    for i in range(len(newArr)):
        newArr[i] = newArr[i][:-2]
        newArr[i] = newArr[i].split(",")
        for number in range(len(newArr[i])):
            newArr[i][number] = int(newArr[i][number])
open('saveLikes.txt', 'w').close()


print(newArr)