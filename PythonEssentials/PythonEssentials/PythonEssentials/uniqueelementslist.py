my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = my_list[]

for el in my_list:
    if el in new_list:     # Alternativa: usar not in,
        continue           # para não usar else
    else:
        new_list.append(el)

print("The list with unique elements only:", new_list)
print("Original list:", my_list)
