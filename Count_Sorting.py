listS = [9, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1]
index_List = []
for i in range(len(listS)):
    index_List.append(listS.count(i))
print(f' Создаем массив индексов {index_List}')

Sorted_ListS = []
for i in range(len(index_List)):
    while index_List[i] > 0:
        Sorted_ListS.append(i)
        index_List[i] -= 1

print(f'Sorted_ListS {Sorted_ListS} ')



