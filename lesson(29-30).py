# sorting algorithms
# cesidleme -> verilmis elementleri mueyyen qaydada siralamaqdir
# Artan qaydada -> kicikden boyuye
# Azalan qaydada -> boyukden kiciye
# sorting methods: .sort()
example_list = [5, 7, 3, 8, 1, 2]
# Artan qaydada
example_list.sort()
print(example_list)
# Azalan qaydada
example_list.sort(reverse=True)
print(example_list)
# Python .sort() metodunun arxa fonunda Timsort adlanan alqoritmden istifade edir
# Timsort alqoritmi Insertion sort ve Merge sort alqoritmlerinin hibrididir.
# Sorting alqoritmlerinin novleri:
# 1) Bubble sort -> artan qaydada
example_list = [7, 5, 3, 8, 1, 2]
for run in range(len(example_list) - 1):
    for i in range(len(example_list) - 1):
        if example_list[i] > example_list[i+1]:
            example_list[i], example_list[i+1] = example_list[i+1], example_list[i]
print(example_list)
# Bubble sort -> azalan qaydada
example_list = [7, 5, 3, 8, 1, 2]
for run in range(len(example_list) - 1):
    for i in range(len(example_list) - 1):
        if example_list[i] < example_list[i+1]:
            example_list[i], example_list[i+1] = example_list[i+1], example_list[i]
print(example_list)



# 2) Insertion sort
example_list = [7, 5, 3, 8, 1, 2]
length = len(example_list)

for i in range(1, length):
    key = example_list[i]
    j = i-1
    while example_list[j] > key and j >= 0:
        example_list[j+1] = example_list[j]
        j = j - 1

    example_list[j + 1] = key

print(example_list)
# 3) Merge sort
# 4) Quick sort