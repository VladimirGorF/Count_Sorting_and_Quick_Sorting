import random
listS = [9, 1, 4, 6, 5, 2]

def Quick_Sorting(listS):
    if len(listS) <= 1:
        return listS
    pivot = random.choice(listS)
    left = [n for n in listS if n < pivot]
    right = [n for n in listS if n > pivot]
    med = [pivot] * listS.count(pivot)
    return Quick_Sorting(left) + med + Quick_Sorting(right)

print(Quick_Sorting(listS))